#!/usr/bin/env python3

import os

import pandas as pd


INPUT_PATH = os.path.join(os.path.dirname(__file__), '../data.csv')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../not-null-data.csv')
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


if __name__ == '__main__':
    # read dataset
    raw_data = pd.read_csv(INPUT_PATH)
    print(f'> read {len(raw_data)} rows.')
    raw_data.rename(columns=COLUMNS_MAP, inplace=True)
    # filter out empty data
    raw_data = raw_data[raw_data.visits != 0]
    # filter out counters without cords
    raw_data = raw_data[~raw_data.counter_id.isin([368, 667, 956, 1209])]
    data = raw_data[COLUMNS]

    data.to_csv(OUTPUT_PATH)
    print(f'> save {len(data)} rows.')
