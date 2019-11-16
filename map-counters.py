from bson.code import Code

from utils import connect


mapper_func = open('counters/mapper.js', 'r').read()
reducer_func = open('counters/reducer.js', 'r').read()


if __name__ == '__main__':
    db = connect()
    db.main.map_reduce(Code(mapper_func), Code(reducer_func), 'counters')
