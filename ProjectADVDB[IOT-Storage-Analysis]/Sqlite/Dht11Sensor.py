import time
import timeit
import sqlite3
import Adafruit_DHT
dbname='sensorsData.db'
sampleFreq = 1*60 # time in seconds ==> Sample each 1 min
# get data from DHT sensor
def getDHTdata():	
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
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	print("Done")
	curs.execute("INSERT INTO DHT_data values( (?), (?),datetime('now'))", (temp, hum))
	conn.commit()
	print("Done Commit")
	conn.close()
	
#print("insert data Time:",timeit.timeit(lambda: logData(25, 50), number=10))

# main function
def main():
	while True:
		temp, hum = getDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)
# ------------ Execute program 
main()
