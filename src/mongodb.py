from pymongo import MongoClient
import pandas as pd
import csv
import json
import os
import datetime
from src.fetch_crypto import *
from datetime import datetime,timezone


# This file is used to store the data from the API into a mongodb database
def insert_assets_data():
    client = MongoClient("mongodb://root:root@mongodb:27017") # mongo is the docker service and has to be corrct.
    db = client.mongo_db
    assets = db['assets']
    list = []
    for i in get_assets():  # each one assets is a dictionary, use for loop to iterate each one
        crypt = {'asset_id': i['asset_id'],
                 'name': i['name'],
                 'price_usd': i['price_usd'], # price in USD
                 'volume_1hrs_usd': i['volume_1hrs_usd'], # last hour coin volume
                 'date': datetime.now(timezone.utc)
                 }
        list.append(crypt)
    print(list)
    assets.insert_many(list) # insert assets data into mongoDB
    client.close() # close mongoDB connection
    print("Successfully Inserted assets data") # print success message

def insert_historical_data():
    client = MongoClient("mongodb://root:root@localhost:27017") # mongo is the docker service and has to be corrct.
    db = client.mongo_db
    historical_price = db['historical_data']
    with open('D:\PycharmProjects\\5400FinalProject\Data\coin.json') as f:
        file_data = json.load(f)
    historical_price.insert_many(file_data) # insert assets data into mongoDB
    client.close() # close mongoDB connection
    print("Successfully Inserted historical_price data") # print success message

def drop_collection():
    client = MongoClient("mongodb://root:root@localhost:27017") # mongo is the docker service and has to be corrct.
    # If run this code local mode, please change the mongo to localhost.
    db = client.mongo_db
    db.drop_collection('USmarket')
    client.close() # close mongoDB connection
    print("Successfully Dropped collection") # print success message

def insert_TBill_data():
    client = MongoClient("mongodb://root:root@localhost:27017")  # mongo is the docker service and has to be corrct.
    # If run this code local mode, please change the mongo to localhost.
    db = client.mongo_db
    tbill = db['tbill']
    list = []
    for i in US_TBill_Interest_Rate():
        bill = {'date': i[0],'rate': i[1]}
        list.append(bill)
    tbill.insert_many(list)  # insert assets data into mongoDB
    client.close()  # close mongoDB connection
    print("successfully Inserted Treasury Bills time series data")  # print success message

def insert_USmarket_data():
    client = MongoClient("mongodb://root:root@localhost:27017")  # mongo is the docker service and has to be corrct.
    # If run this code local mode, please change the mongo to localhost.
    db = client.mongo_db
    USmarket = db['USmarket']
    list = []
    for i in get_US_market_summary():
        if i.__contains__('Name'):
            data = {'Name': i['Name'],
                    'exchange': i['exchange'],
                    'tradeable': i['tradeable'],
                    'customPriceAlertConfidence': i['customPriceAlertConfidence'],
                    'fullExchangeName': i['fullExchangeName'],
                    'exchangeTimezoneName': i['exchangeTimezoneName'],
                    'market': i['market'],
                    'marketState': i['marketState'],
                    'quoteType': i['quoteType'],
                    'region': i['region'],
                    'regularMarketChange': i['regularMarketChange']['fmt'],
                    'regularMarketChangePercent': i['regularMarketChangePercent']['fmt'],
                    'regularMarketPrice': i['regularMarketPrice']['fmt']
                    }
        else:
            data = {'Name':"No short name",
                    'exchange':i['exchange'],
                    'tradeable':i['tradeable'],
                    'customPriceAlertConfidence':i['customPriceAlertConfidence'],
                    'fullExchangeName':i['fullExchangeName'],
                    'exchangeTimezoneName':i['exchangeTimezoneName'],
                    'market':i['market'],
                    'marketState':i['marketState'],
                    'quoteType':i['quoteType'],
                    'region':i['region'],
                    'regularMarketChange':i['regularMarketChange']['fmt'],
                    'regularMarketChangePercent':i['regularMarketChangePercent']['fmt'],
                    'regularMarketPrice':i['regularMarketPrice']['fmt']
                    }
        list.append(data)
    USmarket.insert_many(list)  # insert assets data into mongoDB
    client.close()  # close mongoDB connection
    print("successfully Inserted Treasury Bills time series data")  # print success message

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            # row[1] = int(row[1])
            if row['prev_day_price'] == '': # if there is no previous day price, set it to 0
                row['prev_day_price'] = 0
            if row['daily_return'] == '': # if there is no daily return, set it to 0
                row['daily_return'] = 0
            row["Close"] = float(row["Close"]) # convert close price to float
            row["High"] = float(row["High"])
            row["Low"] = float(row["Low"])
            row["Open"] = float(row["Open"])
            row["Volume"] = float(row["Volume"])
            row["Marketcap"] = float(row["Marketcap"])
            row["prev_day_price"]  = float(row["prev_day_price"])
            row["daily_return"] = float(row["daily_return"])
            jsonArray.append(row) # add this dict to json array
    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
#
#
# csvFilePath = '../Data/coin.csv'
# jsonFilePath = '../Data/coin.json'
# csv_to_json(csvFilePath, jsonFilePath)

# with open('../Data/coin.json') as f:
#     file_data = json.load(f)
#     collection_currency.insert_many(file_data)
#     client.close()
