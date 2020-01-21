# xml-flattener

Turn an xml document into flat files.

# Input

payload.xml: </br>

<code>
<payload>
  <order action="create">
    <orderId>O123</orderId>
    <ticker>IBM</ticker>
    <orderQty>100</orderQty>
    <orderPrice>100.00</orderPrice>
    <orderCurrency>USD</orderCurrency>
    <orderType>BUY</orderType>
    <allocations>
      <allocation action ="create">
        <orderId>O123</orderId>
        <account>111111</account>
        <accountCurrency>USD</accountCurrency>
      </allocation>
      <allocation action ="create">
        <orderId>O123</orderId>
        <account>222222</account>
        <accountCurrency>USD</accountCurrency>
      </allocation>
    </allocations>
  </order>
</payload>
</code>

# Output

order.dat

action|orderCurrency|orderId|orderPrice|orderQty|orderType
"create"|"USD"|"O123"|"100.00"|"100"|"BUY"

allocations.dat

account|accountCurrency|action|orderId
"111111"|"USD"|"create"|"O123"
"222222"|"USD"|"create"|"O123"
