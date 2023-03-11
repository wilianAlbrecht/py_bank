from pymongo import MongoClient

class Connection():

    def __init__(self, table) -> None:
        
        __client = MongoClient("mongodb://localhost:27017")
        __db = __client.bank
        __table = table
        
        
    