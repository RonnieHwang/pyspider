from datetime import datetime
from pymongo import MongoClient


client = MongoClient('mongodb://wisers_dbadmin:K4w3Rmu2@10.36.1.5:27017/research')
research = client['research']


def get_today_str():
    return datetime.now().strftime('%Y-%m-%d')


def get_today():
    today_str = get_today_str()
    return datetime.strptime(today_str, '%Y-%m-%d')
