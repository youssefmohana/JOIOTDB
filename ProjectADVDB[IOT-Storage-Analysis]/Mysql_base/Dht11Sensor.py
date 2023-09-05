import Adafruit_DHT as AD
import time
import timeit
import  mysql.connector as  con
db_config =  {
    'user': 'root',
    'password': 'Jo123',
    'host': 'localhost',
    'database':'Wearher_db',
    }

db_connnection=  con.connect(**db_config)
db_cursor= db_connnection.cursor()

def log_DHT_Sensor():
    # select sensor type [DHT11 ,  DHT22]
    DHT_SENSOR = AD.DHT11

    # GPIO PIN  4 
    DHT_PIN = 4

    while True :
        hum , Temp = AD.read(DHT_SENSOR  , DHT_PIN)
        if hum is not None and Temp is not None :
            sql = "INSERT INTO WEATHER_data (Temp ,hum) VALUES  (%s,%s)"
            values = (Temp , hum)
            db_cursor.execute(sql ,  values)
            db_connnection.commit()
            print("data logged successfully")
 #           break
        else :
            print("faild to retrive  data ^__________________________^")
        time.sleep(1)    
 
#print(timeit.timeit(lambda: log_DHT_Sensor(), number=10))

def close_connection():
    db_cursor.close()
    db_connnection.close()



def Test_DhtSensor():
    
    """for testing sensor with raspi"""
    
    # select sensor type [DHT11 ,  DHT22]
    DHT_SENSOR = AD.DHT11

    # GPIO PIN  4 
    DHT_PIN = 4

    while True :
        hum , Temp = AD.read(DHT_SENSOR  , DHT_PIN)
        if hum is not None and Temp is not None :
            print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(Temp, hum))
        else :
            print("Sensor failure. check wiring .")
        time.sleep(3)

if  __name__ == "__main__":
    try:
        while True :
            log_DHT_Sensor()
    except KeyboardInterrupt:
        close_connection()
    