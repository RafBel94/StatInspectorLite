import time
import logwriting
import databasewriting
import getinfo

if __name__ == "__main__":
    print("Starting monitoring... Press CTRL+C to stop.")
    while True:
        if(int(str(getinfo.get_cpu_temp()).split(",")[0]) > 45):
            logwriting.write_log()
            databasewriting.write_to_database()
        time.sleep(3)