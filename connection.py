from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def getDatabaseWithCollection():
    connection_string = os.getenv("MONGO_CONNECTION_STRING")

    client = MongoClient(connection_string)
    
    collection = client['StatInspectorLite']['st_inspector']
    
    return collection