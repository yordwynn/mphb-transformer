from pymongo import MongoClient


class DataLoader:
    """
    Load image metadata from Mongodb
    """
    def __init__(self, uri='localhost', port=27017):
        self.uri = uri
        self.port = port
        self.client = MongoClient(uri, port)
