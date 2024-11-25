import datetime
import os
import threading
from getinfo import get_cpu_usage, get_gpu_temp, get_memory_usage, get_ip, get_running_tasks

LOG_FILE = 'log.txt'
MAX_ENTRIES = 5

def write_log():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    cpu_usage = gpu_temp = memory_usage = ip_address = running_tasks = None

    def fetch_cpu_usage():
        nonlocal cpu_usage
        cpu_usage = get_cpu_usage()

    def fetch_gpu_temp():
        nonlocal gpu_temp
        gpu_temp = get_gpu_temp()

    def fetch_memory_usage():
        nonlocal memory_usage
        memory_usage = get_memory_usage()

    def fetch_ip():
        nonlocal ip_address
        ip_address = get_ip()

    def fetch_running_tasks():
        nonlocal running_tasks
        running_tasks = len(get_running_tasks())

    threads = [
        threading.Thread(target=fetch_cpu_usage),
        threading.Thread(target=fetch_gpu_temp),
        threading.Thread(target=fetch_memory_usage),
        threading.Thread(target=fetch_ip),
        threading.Thread(target=fetch_running_tasks)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    log_entry = f"{timestamp}\nCPU Usage: {cpu_usage}%\nGPU Temperature: {gpu_temp}C\nRAM Usage: {memory_usage}%\nIP Address: {ip_address}\nRunning Tasks: {running_tasks}\n"

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as file:
            lines = file.readlines()
        
        entries = ''.join(lines).split('\n\n')
        if len(entries) >= MAX_ENTRIES:
            entries = entries[1:]
        entries.append(log_entry.strip())
        
        with open(LOG_FILE, 'w') as file:
            file.write('\n\n'.join(entries))
    else:
        with open(LOG_FILE, 'w') as file:
            file.write(log_entry)