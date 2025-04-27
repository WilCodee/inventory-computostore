import os

from pymongo import MongoClient


class ConnectMongo:
    def __init__(self):
        # Usa variables de entorno para seguridad
        self.uri = os.getenv("MONGO_URI")
        self.db_name = os.getenv("MONGO_DB_NAME")
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]

    def get_collection(self, name_collection):
        return self.db[name_collection]

    def close_connection(self):
        self.client.close()
