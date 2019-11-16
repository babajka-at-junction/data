#!/usr/bin/env python3

import json

import pandas as pd

from cook_data import OUTPUT_PATH
from utils import connect, parse_date


if __name__ == '__main__':
    data = pd.read_csv(OUTPUT_PATH)
    data_json = json.loads(data.to_json(orient='records'))
    data_to_db = []
    for i in range(len(data_json)):
        start = parse_date(data_json[i]['start_at'])

        # get data for last 3 years
        if start.year < 2017:
            continue

        end = parse_date(data_json[i]['end_at'])
        duration = (end - start).total_seconds()
        # for now filter out all non-hourly counts
        if duration != 3600:
            continue

        data_json[i]['start_at'] = start
        data_json[i]['end_at'] = end
        data_json[i]['installed_at'] = parse_date(data_json[i]['installed_at'])
        data_to_db.append(data_json[i])

    # save to mongo
    db = connect()
    db.main.delete_many({})
    db.main.insert_many(data_to_db)

    print(f'Successfully insert {len(data_to_db)} documents. ({len(data) - len(data_to_db)} filtered)')
