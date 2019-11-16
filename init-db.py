#!/usr/bin/env python3

import os
import json
import pandas as pd
from pymongo import MongoClient

FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')


def connect():
    client = MongoClient()
    db=client['junc19']
    collection = db['main']
    return collection


if __name__ == '__main__':
    # read dataset
    data = pd.read_csv(FILE_PATH)
    # remove `.` from columns names
    data.columns = list(map(lambda x: x.replace('.', '__'), data.columns))
    data_json = json.loads(data.to_json(orient='records'))

    # save to mongo
    collection = connect()
    collection.delete_many()
    collection.insert_many(data_json)

    print(f'Successfully insert {len(data_json)} documents.')
