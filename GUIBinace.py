from tkinter import *

######################################

from binance.client import Client
from pprint import pprint
import time
import Key

api_key = Key.api_key
api_secret = Key.api_secret

client = Client(api_key, api_secret)

doge = client.get_asset_balance(asset='DOGE')
usdt = client.get_asset_balance(asset='USDT')

text_doge = '{} : {} (In orfer: {})'.format(doge['asset'], doge['free'], doge['locked'])
text_usdt = '{} : {} (In orfer: {})'.format(usdt['asset'], usdt['free'], usdt['locked'])
alltext = text_doge + '\n' + text_usdt

def UpdatePrice() :
    prices = client.get_all_tickers()
    current_price = ''
    coin_name = 'DOGEUSDT'

    for p in prices :
        if p['symbol'] == coin_name :
            current_price = p
            
    time.sleep(0.2)
    #{'symbol' : 'DOGEUSDT', 'price' : '0.523425'}
    v_current.set('{} : {}'.format(current_price['symbol'], current_price['price']))
    R1.after(100,UpdatePrice)

#######################################

GUI =Tk()
GUI.geometry('700x300')
GUI.title('Program Crypto by Apichai Thinthonglang')

FONT1 = ('Angsana New', 25)

L = Label(GUI, text='Total Price', font=FONT1)
L.pack()

v_balance = StringVar()
v_balance.set(alltext)

BL = Label(GUI, textvariable=v_balance, font=FONT1, fg='green')
BL.pack()

v_current = StringVar()

R1 = Label(GUI, textvariable=v_current, font=FONT1, fg='blue')
R1.pack()

UpdatePrice()

GUI.mainloop()
