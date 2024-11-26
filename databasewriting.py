import connection, getinfo
import datetime
import threading

collection = connection.getDatabaseWithCollection()

MAX_ENTRIES = 5000

def write_to_database():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    gpu_temp = cpu_temp = memory_usage = ip_address = running_tasks = None

    def fetch_gpu_temp():
        nonlocal gpu_temp
        gpu_temp = getinfo.get_gpu_temp()
        
    def fetch_cpu_temp():
        nonlocal cpu_temp
        cpu_temp = getinfo.get_cpu_temp()

    def fetch_memory_usage():
        nonlocal memory_usage
        memory_usage = getinfo.get_memory_usage()

    def fetch_ip():
        nonlocal ip_address
        ip_address = getinfo.get_ip()

    def fetch_running_tasks():
        nonlocal running_tasks
        running_tasks = len(getinfo.get_running_tasks())

    threads = [
        threading.Thread(target=fetch_gpu_temp),
        threading.Thread(target=fetch_cpu_temp),
        threading.Thread(target=fetch_memory_usage),
        threading.Thread(target=fetch_ip),
        threading.Thread(target=fetch_running_tasks)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    log_entry = {
        "timestamp": timestamp,
        "gpu_temp": gpu_temp,
        "cpu_temp": int(str(cpu_temp).split(",")[0]),
        "memory_usage": memory_usage,
        "ip_address": ip_address,
        "running_tasks": running_tasks
    }

    last_entry = collection.find_one(sort=[("_id", -1)])
    new_id = last_entry["_id"] + 1 if last_entry else 1
    log_entry["_id"] = new_id

    if collection.count_documents({}) < MAX_ENTRIES:
        collection.insert_one(log_entry)