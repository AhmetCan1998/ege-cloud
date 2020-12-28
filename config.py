import json

from meta.singleton import Singleton


class Configuration(metaclass=Singleton):
    def __init__(self, name):
        with open(name, "r") as file:
            self.config = json.load(file)

    "database": {
        "host" : "ahmetpostgres1966.postgres.database.azure.com",
        "dbname" : "postgres",
        "user" : "ahmet1998",
        "password" : "Balkes.1998",
        "ssl" : "require"
    }