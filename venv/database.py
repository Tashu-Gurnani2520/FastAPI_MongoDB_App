
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://TashuGurnani:SMhOjWQtFUahafB2@destiny.4bssk.mongodb.net/?retryWrites=true&w=majority&appName=Destiny"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db  =  client["e-commerce"]