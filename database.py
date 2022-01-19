from time import asctime, time
import uuid

from tinydb import TinyDB, Query
db = TinyDB('db.json')


def save_data_to_db():

    timestamp = asctime()
    _id = str(uuid.uuid4())

    # save data in a dictionary
    data = {timestamp: _id}

    # save info to datbase
    db.insert(data)


def get_data_from_db():
    # get all data in database
    data = db.all()

    # reverse data
    data.reverse()

    return data
