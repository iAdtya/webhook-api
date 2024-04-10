import os
from pymongo.mongo_client import MongoClient

## i know i am not using .env cz its shared resource
uri = "mongodb+srv://adityakhedekar98906:K6m89IUHPUTnV5Xh@stax-db.phjk2qm.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

