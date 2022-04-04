# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import schedule
import time
from src.fetch_crypto import get_coin_data
from src.postgredb import *
from src.fetch_crypto import *
import os


def job():
    insert_coindata(get_coin_data())

if __name__ == '__main__':
    schedule.every(60).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)