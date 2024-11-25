import connection

collection = connection.getDatabaseWithCollection()

def insertData(name, age, city):
    
    if collection.count_documents({}) >= 5000:
        print("Database is full, please erase some data")
    else:
        collection.insert_one({"name": name, "age": age, "city": city})
        
insertData("Pablo", 99, "Pontevedra")