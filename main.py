import connection
import time
import logwriting
import databasewriting

def obtener_temperatura_cpu(url="http://localhost:8085/data.json"):
    try:
        # Solicitar datos del servidor de OpenHardwareMonitor
        response = requests.get(url)
        data = response.json()
        
        # Recorrer los sensores para encontrar la temperatura de la CPU
        for hardware in data['Children']:
            for sensor in hardware['Children']:
                if sensor['Text'] == 'Intel Core i7-9850H': # Replace with your CPU model
                    for core in sensor['Children']:
                        for temp in core['Children']:
                            if temp['Text'] == 'Temperatures':
                                return core['Value']
                            
        else:
            print("No se encontraron sensores de temperatura para la CPU.")
    except Exception as e:
        print(f"Error al obtener los datos: {e}")

while True:
    logwriting.write_log()
    databasewriting.write_to_database()
    time.sleep(2)