import socket
import psutil
import pynvml

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_gpu_usage():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetUtilizationRates(handle)
    return info.gpu

def get_gpu_temp():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetTemperature(handle, 0)
    return info

def get_running_tasks():
    tasks = []
    for proc in psutil.process_iter(['pid', 'name']):
        tasks.append(proc.info)
    return tasks
