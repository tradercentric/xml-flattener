import time

from lxml import etree


def get_dict_list(root, config_item):
    entity_name = config_item[0]
    include_attributes = config_item[1]
    include_elements = config_item[2]
    entities = root.findall('.//' + entity_name)
    records = []
    for e in entities:
        this = {}
        for key in include_attributes:
            this[key] = None
            if key in e.attrib.keys():
                this[key] = e.attrib[key]
        for el in include_elements:
            this[el.split('/')[-1]] = None
            if e.find(el) != None:
                this[e.find(el).tag] = e.find(el).text
        records.append(this)
    return records


def process_file(in_file, target, out_file, configItems):
    print("Input file : %s" % in_file)
    root = etree.parse(in_file).getroot()
    keys = []
    records = []
    for configItem in configItems:
        if configItem[0] == target:
            records = get_dict_list(root, configItem)
            if len(records) == 0:
                print("No record found for target: %s" % target)
                return
            for k in records[0].keys():
                keys.append(k)
    keys = sorted(keys)
    header = '|'.join(keys)
    text_file = open(out_file, "w")
    text_file.write("{0}\n".format(header))

    for r in records:
        fields = []
        for k in keys:
            v = r[k]
            if v is None:
                fields.append('')
            else:
                v = '"' + v.strip('|').strip('\n').strip('"') + '"'
                fields.append(v)
        detail = '|'.join(fields)
        text_file.write("{0}\n".format(detail))
    text_file.close()
    print("Output file: %s" % out_file)


if __name__ == '__main__':
    # begin configuration
    configItems = [  # configuration for investment portfolio
        ['order',
         {'action'},
         {'orderId',
          'orderQty',
          'orderPrice',
          'orderCurrency',
          'orderType'
          }
         ],
        ['allocations/allocation',
         {'action'},
         {'orderId',
          'account',
          'accountCurrency'
          }
        ]
    ]
    # end configuration
    # program parameter

    start = time.time()

    process_file('./payload.xml', 'order', './order.dat', configItems)
    process_file('./payload.xml', 'allocations/allocation', './allocations.dat', configItems)

    end = time.time()
    print("Elapsed (s): %d" % (end - start))
