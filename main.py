import connection
import time
import logwriting
import databasewriting

collection = connection.getDatabaseWithCollection()

while True:
    logwriting.write_log()
    databasewriting.write_to_database()
    time.sleep(2)