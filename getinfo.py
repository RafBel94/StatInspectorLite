import socket
import psutil
import pynvml
import requests

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

def get_cpu_temp(url="http://localhost:8085/data.json"):
    try:
        # Get JSON response from Open Hardware Monitor
        response = requests.get(url)
        data = response.json()
        
        # Find the CPU temperature sensor and get CPU temperature value
        for hardware in data['Children']:
            for sub_hardware in hardware['Children']:
                if sub_hardware['Text'] == "Intel Core i7-9850H":
                    for sensor in sub_hardware['Children']:
                        if sensor['Text'] == "Temperatures":
                            for temp_sensor in sensor['Children']:
                                if temp_sensor['Text'] == "CPU Core #1":
                                    return temp_sensor['Value']
                                
        else:
            print("There are no CPU temperature sensors")
    except Exception as e:
        print(f"Error obtaining temperature: {e}")

def get_running_tasks():
    tasks = []
    for proc in psutil.process_iter(['pid', 'name']):
        tasks.append(proc.info)
    return tasks