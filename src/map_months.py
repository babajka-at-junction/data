#!/usr/bin/env python3
import os
import json

from bson.code import Code

from utils import connect


mapper_func = open('src/months/mapper.js', 'r').read()
reducer_func = open('src/months/reducer.js', 'r').read()


if __name__ == '__main__':
    db = connect()
    months = db.main.map_reduce(Code(mapper_func), Code(reducer_func), 'months')
    outpath = os.path.join(os.path.dirname(__file__), '../months.json')
    with open(outpath, 'w') as outfile:
        json.dump(list(months.find()), outfile)
