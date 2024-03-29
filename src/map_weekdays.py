#!/usr/bin/env python3
import os
import json

from bson.code import Code

from utils import connect


mapper_func = open('src/weekdays/mapper.js', 'r').read()
reducer_func = open('src/weekdays/reducer.js', 'r').read()


if __name__ == '__main__':
    db = connect()
    weekdays = db.main.map_reduce(Code(mapper_func), Code(reducer_func), 'weekdaysByCounter')
    outpath = os.path.join(os.path.dirname(__file__), '../weekdays.json')
    result = {}
    for doc in weekdays.find():
        v = doc['value']
        id, weekday, visits = int(v['id']), v['weekday'], int(v['visits'])
        result[id] = result.get(id, {})
        result[id][weekday] = visits

    with open(outpath, 'w') as outfile:
        json.dump(result, outfile)
