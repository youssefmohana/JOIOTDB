import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con: 
    cur = con.cursor() 
    cur.execute("CREATE TABLE DHT_data(temp NUMERIC, hum NUMERIC,timestamp DATETIME)")
