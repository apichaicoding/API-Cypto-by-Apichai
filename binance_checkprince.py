from binance.client import Client
import time
from pprint import pprint
import Key

api_key = Key.api_key
api_secret = Key.api_secret

client = Client(api_key, api_secret)

while True :
    prices = client.get_all_tickers()
    current_prince = ''
    coin_name = 'DOGEUSDT'

    for p in prices :
        if p['symbol'] == coin_name :
            current_prince = p
    print(current_prince)
    time.sleep(0.2)
