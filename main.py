import time
import logwriting
import databasewriting

if __name__ == "__main__":
    print("Starting monitoring...")
    
    while True:
        logwriting.write_log()
        databasewriting.write_to_database()
        time.sleep(3)