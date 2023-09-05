from datetime import datetime
from tinydb import TinyDB, Query
import time 
import Adafruit_DHT
import timeit

db = TinyDB('sensor_data.json')
sampleFreq = 1*60 # time in seconds ==> Sample each 1 min
sensor_data_table = db.table('sensor_data')

def insertDHTdata():	
	DHT11Sensor = Adafruit_DHT.DHT11
	DHTpin = 4
	hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
		print(hum , temp)
	return temp, hum
# log sensor data on database
def logData (temp, hum):
    
    sensor_data_table.insert({
        'temperature': temp,
        'humidity': hum,
        'timestamp': datetime.now().isoformat()
    })

    print("Done")

#print("insert data Time:",timeit.timeit(lambda: logData(25, 50), number=10))

def main():
	while True:
		temp, hum = insertDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)
# ------------ Execute program 
main()
