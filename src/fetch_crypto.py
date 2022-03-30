import requests
import pandas as pd
from requests.exceptions import HTTPError
import yfinance as yf
from pprint import pprint
import datetime
import json
import psycopg2.extras as p
"""
This module is used to get cryptocurrency data from coincap API.
"""

# Get
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

def get_coin_exchange_data():
    try:
        url = "http://api.coincap.io/v2/exchanges/bitcoin"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return pprint(response.json()['data'])

def get_coin_history():
    try:
        url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=m1"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
    except HTTPError as http_err:
        print(f'HTTP error occurred:{http_err}')
    except Exception as err:
        print(f'Other error occurred:{err}')
    return response.json()