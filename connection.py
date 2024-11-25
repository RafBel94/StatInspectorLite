import pymongo
from pymongo import MongoClient

def getDatabaseWithCollection():
    connection_string = "mongodb+srv://rafaelbeltrancaceres:8uT61KbtjS8C4u4s@mycluster.2ezw4.mongodb.net/"

    client = MongoClient(connection_string)
    
    collection = client['StatInspectorLite']['st_inspector']
    
    return collection;

# This is added so many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = getDatabaseWithCollection()