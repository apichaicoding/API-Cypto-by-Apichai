from binance.client import Client
from pprint import pprint
import time
import Key

api_key = Key.api_key
api_secret = Key.api_secret

client = Client(api_key, api_secret)

#Order
'''
order = client.order_limit_buy(
    symbol='DOGEUSDT',
    quantity=500,
    price='0.03')

pprint(orders)
'''

#Cancel Order
''''
result = client.cancel_order(
    symbol='BNBBTC',
    orderId='orderId')
    pprint(orders)
'''

orders = client.get_open_orders(symbol='DOGEUSDT')
print('ALL ORDERS', orders)
