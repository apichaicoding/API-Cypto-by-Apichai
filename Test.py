from binance.client import Client
import time
from datetime import datetime, timedelta
from time import mktime
from pprint import pprint

api_key = ''
api_secret = ''

client = Client(api_key,api_secret)
print('OK')

time_res = client.get_server_time()
tm = time_res['serverTime']/1000

dt = datetime.fromtimestamp(mktime(time.localtime(tm)))
dt = dt + timedelta(hours=7)
dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print(dt)

#status = client.get_system_status()
#print(status)

#info = client.get_symbol_info('BTCUSDT')
#pprint(info)

#tickers = client.get_ticker(symbol='BTCUSDT')
#pprint(tickers)

#print('Price Sell Less: ', tickers['askPrice'])

#prices = client.get_all_tickers()
#print(prices)
#print('COUNT: ',len(prices))

#for pc in prices:
#    if pc['symbol'] == 'ETCBTC':
#        print(pc)

#depth = client.get_order_book(symbol='SUSDBTC',limit=5)
#pprint(depth)
#print(len(depth['asks']))

#trades = client.get_recent_trades(symbol='SUSDBTC',limit=5)
#current = []
#for t in trades:
#    current.insert(0,t)
#pprint(current)

#candles = client.get_klines(symbol='SUSDBTC', interval=Client.KLINE_INTERVAL_30MINUTE, limit=5)
#pprint(candles)

orders = client.get_all_orders(symbol='BTCUSDT', limit=10)
#pprint(orders)
allbuy =[]
for od in orders:
    if od['side'] == 'BUY' and od['status'] == 'NEW':
        allbuy.append(od)
if len(allbuy) > 1:
    print('buy')
else:
    print('awit buy')
print(allbuy)
