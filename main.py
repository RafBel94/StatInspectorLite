import connection
import time
import logwriting

collection = connection.getDatabaseWithCollection()

def insertData(name, age, city):
    
    if collection.count_documents({}) >= 5000:
        print("Database is full, please erase some data")
    else:
        collection.insert_one({"name": name, "age": age, "city": city})
        
while True:
    logwriting.write_log()
    time.sleep(2)