import requests
import json


def get_value():
    url = "https://blockchain.info/ticker"

    response = requests.get(url)
    value = json.loads(response.text)["TRY"]["15m"]

    return value
