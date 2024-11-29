import datetime
import os
import threading
import telegram_utils
from getinfo import get_gpu_temp, get_memory_usage, get_ip, get_running_tasks, get_cpu_temp

LOG_FILE = 'log.txt'
MAX_ENTRIES = 5

def write_log():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    gpu_temp = memory_usage = ip_address = running_tasks = cpu_temp = None

    def fetch_gpu_temp():
        nonlocal gpu_temp
        gpu_temp = get_gpu_temp()
    
    def fetch_cpu_temp():
        nonlocal cpu_temp
        cpu_temp = get_cpu_temp()

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
    
    log_entry = f"{timestamp}\nGPU Temperature: {gpu_temp}C\nCPU Temperature: {str(cpu_temp).split(",")[0]}C\nRAM Usage: {memory_usage}%\nIP Address: {ip_address}\nRunning Tasks: {running_tasks}\n"

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
            
    # Send telegram message
    telegram_utils.send_message(log_entry)