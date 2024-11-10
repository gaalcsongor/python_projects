# FXRates API

import requests

r = requests.get("https://api.fxratesapi.com/latest")

data = r.json()

rate_usd_huf = data["rates"]["HUF"]

print(rate_usd_huf)
print(type(rate_usd_huf))