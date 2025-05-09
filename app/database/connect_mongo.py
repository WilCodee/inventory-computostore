import os

from pymongo import MongoClient


class ConnectMongo:
    def __init__(self):
        # Usa variables de entorno para seguridad
        self.__uri = os.getenv("MONGO_URI")
        self.__db_name = os.getenv("MONGO_DB_NAME")
        self.__client = MongoClient(self.__uri)
        self.__db = self.__client[self.__db_name]

    def get_collection(self, name_collection):
        return self.__db[name_collection]

    def close_connection(self):
        self.__client.close()
