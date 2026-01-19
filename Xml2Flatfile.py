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
            this[key] = e.attrib.get(key)
        for el in include_elements:
            found = e.find(el)
            this[el.split('/')[-1]] = found.text if found is not None else None
        records.append(this)
    return records


def process_file(in_file, target, out_file, configItems):
    print(f"Input file : {in_file}")
    root = etree.parse(in_file).getroot()
    keys = []
    records = []
    for configItem in configItems:
        if configItem[0] == target:
            records = get_dict_list(root, configItem)
            if len(records) == 0:
                print(f"No record found for target: {target}")
                return
            keys = sorted(records[0].keys())
    header = '|'.join(keys)

    with open(out_file, "w") as text_file:
        text_file.write(f"{header}\n")

        for r in records:
            fields = []
            for k in keys:
                v = r[k]
                if v is None:
                    fields.append('')
                else:
                    v = '"' + v.replace('|', '').replace('\n', '').replace('"', '') + '"'
                    fields.append(v)
            detail = '|'.join(fields)
            text_file.write(f"{detail}\n")

    print(f"Output file: {out_file}")


if __name__ == '__main__':
    # begin configuration
    configItems = [  # configuration for investment portfolio
        ['order',
         {'action'},
         {'orderId',
          'ticker',
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
    print(f"Elapsed (s): {end - start:.3f}")
