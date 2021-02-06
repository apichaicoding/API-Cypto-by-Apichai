from binance.client import Client
from pprint import pp

import Key

api_key = Key.api_key
api_secret = Key.api_secret

client = Client(api_key, api_secret)

doge = client.get_asset_balance(asset='DOGE')
usdt = client.get_asset_balance(asset='USDT')

print('DOGE: ', doge)
print('USDT: ', usdt)
