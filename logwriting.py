import datetime
import os
from getinfo import get_cpu_usage, get_gpu_temp, get_memory_usage, get_ip

LOG_FILE = 'log.txt'
MAX_ENTRIES = 5

def write_log():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    cpu_usage = get_cpu_usage()
    gpu_temp = get_gpu_temp()
    memory_usage = get_memory_usage()
    ip_address = get_ip()

    log_entry = f"{timestamp}\nCPU Usage: {cpu_usage}%\nGPU Temperature: {gpu_temp}C\nRAM Usage: {memory_usage}%\nIP Address: {ip_address}\n"

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