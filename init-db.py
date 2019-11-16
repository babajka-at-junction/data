#!/usr/bin/env python3

import os
import json

import pandas as pd
from pymongo import MongoClient


from utils import parse_date
from credentials import DB_HOST


FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')
COLUMNS_MAP = {
    'CounterID_ASTA': 'counter_id',
    'StartTime': 'start_at',
    'EndTime': 'end_at',
    'Visits': 'visits',
    'ASTA_Counters.InstallationDate': 'installed_at',
    'ASTA_Counters.NationalParkCode': 'park_code',
    'PAVE_Counters.CoordinateNorth': 'cord_north',
    'PAVE_Counters.CoordinateEast': 'cord_east',
}
COLUMNS = list(COLUMNS_MAP.values())


def connect():
    client = MongoClient(DB_HOST)
    db=client['junc19']
    collection = db['main']
    return collection


if __name__ == '__main__':
    # read dataset
    raw_data = pd.read_csv(FILE_PATH)
    raw_data.rename(columns=COLUMNS_MAP, inplace=True)
    # filter out empty data
    raw_data = raw_data[raw_data.visits != 0]
    data = raw_data[COLUMNS]

    for i, row in data.iterrows():
        data.at[i, 'start_at'] = parse_date(data.at[i, 'start_at'])
        data.at[i, 'end_at'] = parse_date(data.at[i, 'end_at'])
        data.at[i, 'installed_at'] = parse_date(data.at[i, 'installed_at'])

    data_json = json.loads(data.to_json(orient='records'))

    # save to mongo
    collection = connect()
    collection.remove()
    collection.insert(data_json)

    print(f'Successfully insert {len(data_json)} documents.')
