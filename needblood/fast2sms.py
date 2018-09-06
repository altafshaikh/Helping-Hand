import requests

url = "https://www.fast2sms.com/dev/bulk"
numbers=['9922716338','7020461215']

for number in numbers:
    
    payload = "sender_id=FSTSMS&message=yo bro&language=english&route=p&numbers="+number
    headers = {
    'authorization': "Xn4BP6YkCtab0iTuSgH8WEzJONveKUpIhwARlDx3MZroqFcmVQcD8kBNCzfen2FPpIlsHtZKmJ47X9gi",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)