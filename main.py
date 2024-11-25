import connection
import time
import logwriting
import databasewriting

while True:
    logwriting.write_log()
    databasewriting.write_to_database()
    time.sleep(2)