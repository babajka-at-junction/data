from pyproj import CRS, Transformer

from utils import connect


crs_3067 = CRS.from_epsg(3067)
crs_4326 = CRS.from_epsg(4326) # WGS 84
transformer = Transformer.from_crs(crs_3067, crs_4326)


if __name__ == '__main__':
    db = connect()
    for doc in db.counters.find():
        value = doc['value']
        (e, n) = value['cord_east'], value['cord_north']
        (lat, long) = transformer.transform(e, n)
        doc['lat'] = lat
        doc['long'] = long
        db.counters.update_one(
            { '_id': doc['_id'] },
            { '$set': doc}
        )
