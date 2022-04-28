import requests
import pandas as pd
from requests.exceptions import HTTPError
import yfinance as yf
from pprint import pprint
import datetime
import json
import psycopg2.extras as p

# This file is used to get the latest data from the API
def get_coin_data():
    try:
        url = "http://api.coincap.io/v2/assets/"
        payload = {}
        headers = {}
        response = requests.request("GET",url,headers=headers,data=payload)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return response.json()['data']


def get_assets():
    try:
        url = 'https://rest.coinapi.io/v1/assets/BTC;ETH;XRP;LTC;BCH;EOS;XLM;ADA;TRX;NEO;XMR;IOTA;MIOTA;DASH;ETC;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL;BTS;XLM;XMR;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL;BTS;XLM;XMR;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL;BTS;XLM;XMR;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL;BTS;XLM;XMR;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL;BTS;XLM;XMR;XEM;XVG;ZEC;BTG;USDT;QTUM;LSK;STRAT;ZRX;OMG;BAT;BNB;DOGE;BTS;VEN;DCR;PPT;WAVES;XZC;BCD;ICX;ZIL'
        headers = {'X-CoinAPI-Key': '8742EA5F-8225-4EE7-B553-6DE6B7FD4559'}
        response = requests.get(url, headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return response.json()


def get_US_market_summary():
    try:
        url = "https://yfapi.net/v6/finance/quote/marketSummary?lang=en&region=US"
        headers = {"X-API-KEY": "x1DpiX7tws4GnkH8bpxl38NZYdrBboiB73ETlHDR"}
        response = requests.request("GET",url,headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return response.json()['marketSummaryResponse']['result']

def US_TBill_Interest_Rate():
    try:
        url = "https://data.nasdaq.com/api/v3/datasets/FRED/DTB3.json?Pzuf_8yAvPuv3zgXxTjB"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return response.json()['dataset']['data']
