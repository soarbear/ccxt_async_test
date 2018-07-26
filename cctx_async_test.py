# -*- coding: utf-8 -*-
import asyncio, os, sys
from time import time

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')
sys.path.append('/usr/local/lib/python3.6/site-packages/ccxt')
import ccxt.async_support as ccxt
 
PAIRS = ['BTC/JPY', 'BCH/JPY', 'XEM/JPY', 'MONA/JPY']
 
async def test(exchange, pair):
    print(await exchange.fetch_ticker(pair))
    if pair == 'MONA/JPY': await exchange.close()
 
def main():
    zaif = ccxt.zaif()
    start_time = time()
    asyncio.get_event_loop().run_until_complete(test(zaif, 'BTC/JPY'))
    mid_time = time()
    [asyncio.get_event_loop().run_until_complete(test(zaif, pair)) for pair in PAIRS]
    print(f"[info]downloaded time of 1 pair :{mid_time-start_time}s")
    print(f"[info]downloaded time of 4 pairs:{time()-mid_time}s")
 
if __name__ == '__main__':
    main()
