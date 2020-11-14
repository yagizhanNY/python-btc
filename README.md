## BTC Currency App with Python 3.8

This app for get BTC's current currency from [blockchain.info](https://blockchain.info) site and analyze received data. If received data is changed at the desired percent than app is sends e-mail notification to user.

#### Change the Percent Value

You can change the desire percent value from 

```python
from AnalyzeManager import analyze_change
analyze_change.analyze(current_value, last_value, 0.10)
``` 
this function. The last parameter is desired percent value.

#### Configure E-Mail Settings

In MailManager module you can change youe e-mail parameters like;

* SMTP server
* SMTP server's port
* Sender mail address
* Receiver mail address
* Host's mail username
* Host's mail password
* Mail subject
* Mail body.

Defaults are;

```python
port = 587
smtp_server = "smtp.gmail.com"
sender_mail = "btcservice@yny.com"
receiver_mail = "yagizhanyakali@gmail.com"
username = "***"
password = "***"
subject = "Subject: Guncel BTC Degeri Hakkinda"
body = "BTC guncel degeri: {}TL\nDegisim Yuzdesi: {}".format(str(value), str(change_percent))
```

#### Change Currency Settings

You can also change your current currency from **ApiClient** module;

```python
def get_value():
    url = "https://blockchain.info/ticker"

    response = requests.get(url)
    value = json.loads(response.text)["TRY"]["15m"]

    return value
```

Default currency is **TRY** you can change your main currency. Supported currencies are;

 ```json
{
  "USD" : {"15m" : 15943.93, "last" : 15943.93, "buy" : 15943.93, "sell" : 15943.93, "symbol" : "$"},
  "AUD" : {"15m" : 21930.39, "last" : 21930.39, "buy" : 21930.39, "sell" : 21930.39, "symbol" : "$"},
  "BRL" : {"15m" : 87029.96, "last" : 87029.96, "buy" : 87029.96, "sell" : 87029.96, "symbol" : "R$"},
  "CAD" : {"15m" : 20932.31, "last" : 20932.31, "buy" : 20932.31, "sell" : 20932.31, "symbol" : "$"},
  "CHF" : {"15m" : 14555.55, "last" : 14555.55, "buy" : 14555.55, "sell" : 14555.55, "symbol" : "CHF"},
  "CLP" : {"15m" : 1.22305985E7, "last" : 1.22305985E7, "buy" : 1.22305985E7, "sell" : 1.22305985E7, "symbol" : "$"},
  "CNY" : {"15m" : 105332.01, "last" : 105332.01, "buy" : 105332.01, "sell" : 105332.01, "symbol" : "¥"},
  "DKK" : {"15m" : 100373.44, "last" : 100373.44, "buy" : 100373.44, "sell" : 100373.44, "symbol" : "kr"},
  "EUR" : {"15m" : 13489.64, "last" : 13489.64, "buy" : 13489.64, "sell" : 13489.64, "symbol" : "€"},
  "GBP" : {"15m" : 12083.32, "last" : 12083.32, "buy" : 12083.32, "sell" : 12083.32, "symbol" : "£"},
  "HKD" : {"15m" : 123621.29, "last" : 123621.29, "buy" : 123621.29, "sell" : 123621.29, "symbol" : "$"},
  "INR" : {"15m" : 1188427.37, "last" : 1188427.37, "buy" : 1188427.37, "sell" : 1188427.37, "symbol" : "₹"},
  "ISK" : {"15m" : 2177144.22, "last" : 2177144.22, "buy" : 2177144.22, "sell" : 2177144.22, "symbol" : "kr"},
  "JPY" : {"15m" : 1669368.18, "last" : 1669368.18, "buy" : 1669368.18, "sell" : 1669368.18, "symbol" : "¥"},
  "KRW" : {"15m" : 1.767584406E7, "last" : 1.767584406E7, "buy" : 1.767584406E7, "sell" : 1.767584406E7, "symbol" : "₩"},
  "NZD" : {"15m" : 23282.62, "last" : 23282.62, "buy" : 23282.62, "sell" : 23282.62, "symbol" : "$"},
  "PLN" : {"15m" : 60397.06, "last" : 60397.06, "buy" : 60397.06, "sell" : 60397.06, "symbol" : "zł"},
  "RUB" : {"15m" : 1232466.11, "last" : 1232466.11, "buy" : 1232466.11, "sell" : 1232466.11, "symbol" : "RUB"},
  "SEK" : {"15m" : 138573.52, "last" : 138573.52, "buy" : 138573.52, "sell" : 138573.52, "symbol" : "kr"},
  "SGD" : {"15m" : 21496.57, "last" : 21496.57, "buy" : 21496.57, "sell" : 21496.57, "symbol" : "$"},
  "THB" : {"15m" : 480810.32, "last" : 480810.32, "buy" : 480810.32, "sell" : 480810.32, "symbol" : "฿"},
  "TRY" : {"15m" : 122170.4, "last" : 122170.4, "buy" : 122170.4, "sell" : 122170.4, "symbol" : "₺"},
  "TWD" : {"15m" : 454402.12, "last" : 454402.12, "buy" : 454402.12, "sell" : 454402.12, "symbol" : "NT$"}
}
```

> For more information or support please contact with me at [yagizhanyakali@gmail.com](mailto:yagizhanyakali@gmail.com)