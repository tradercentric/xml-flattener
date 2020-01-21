# xml-flattener

Turn an xml document into flat files.</br>

# Input

payload.xml: </br>

<pre>
<code>
&lt;payload&gt;
  &lt;order action="create"&gt;
    &lt;orderId&gt;O123&lt;/orderId&gt;
    &lt;ticker&gt;IBM&lt;/ticker&gt;
    &lt;orderQty&gt;100&lt;/orderQty&gt;
    &lt;orderPrice&gt;100.00&lt;/orderPrice&gt;
    &lt;orderCurrency&gt;USD&lt;/orderCurrency&gt;
    &lt;orderType&gt;BUY&lt;/orderType&gt;
    &lt;allocations&gt;
      &lt;allocation action ="create"&gt;
        &lt;orderId&gt;O123&lt;/orderId&gt;
        &lt;account&gt;111111&lt;/account&gt;
        &lt;accountCurrency&gt;USD&lt;/accountCurrency&gt;
      &lt;/allocation&gt;
      &lt;allocation action ="create"&gt;
        &lt;orderId&gt;O123&lt;/orderId&gt;
        &lt;account&gt;222222&lt;/account&gt;
        &lt;accountCurrency&gt;USD&lt;/accountCurrency&gt;
      &lt;/allocation&gt;
    &lt;/allocations&gt;
  &lt;/order&gt;
&lt;/payload&gt;
</code>
</pre>

# Output

order.dat </br>

action|orderCurrency|orderId|orderPrice|orderQty|orderType</br>
"create"|"USD"|"O123"|"100.00"|"100"|"BUY"</br>

allocations.dat</br>

account|accountCurrency|action|orderId</br>
"111111"|"USD"|"create"|"O123"</br>
"222222"|"USD"|"create"|"O123"</br>
