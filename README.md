# xml-flattener

Turn an xml document into flat files.</br>

# Input

payload.xml: </br></br>

<pre>
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
</pre>

# Output

order.dat </br></br>

action|orderCurrency|orderId|orderPrice|orderQty|orderType</br>
"create"|"USD"|"O123"|"100.00"|"100"|"BUY"</br>

allocations.dat</br></br>

account|accountCurrency|action|orderId</br>
"111111"|"USD"|"create"|"O123"</br>
"222222"|"USD"|"create"|"O123"</br>
