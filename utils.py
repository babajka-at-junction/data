from datetime import datetime


DATE_FORMAT = '%m/%d/%y %H:%M'


def parse_date(s):
    if type(s) is not str:
        return None
    return datetime.strptime(s, DATE_FORMAT)
