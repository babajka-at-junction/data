from datetime import datetime
from pymongo import MongoClient

# from credentials import DB_HOST


DATE_FORMAT = '%m/%d/%y %H:%M'
DB_NAME = 'junc19'

def parse_date(s):
    if type(s) is not str:
        return None
    return datetime.strptime(s, DATE_FORMAT)


def connect():
    client = MongoClient()
    return client[DB_NAME]
