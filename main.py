# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import schedule
import time
from src.fetch_crypto import get_coin_data
from src.postgredb import *
from src.fetch_crypto import *
from src.mongodb import *
import os
from datetime import datetime

def job_1(): # fetch data from Coin api and insert into mongodb
    insert_assets_data()

def job_2(): # fetch data from coincap api and insert into postgres
    insert_coindata(get_coin_data())

if __name__ == '__main__':
    schedule.every(10).minutes.do(job_1) # run every 10 minutes
    while True:
        schedule.run_pending()
        time.sleep(1)