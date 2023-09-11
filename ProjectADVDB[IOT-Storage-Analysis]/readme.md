#  IOT storage and Anaylsize

1. Use mysql with flask to make iot storage
2. Use Sqllite with flask to make iot storage
3. use TinyDB and Flask (add with caching and without caching)


## MYSQL
1. install mysql (mariiadb for rasperpi lightwieght) and create table caller (Weathe_data) and get code from adufruit (DHT11)

to install mysql in rasperpi:
```
sudo apt install mariadb-server -y
```
    
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using: 
```
pip install -r requirements.txt
```
2. use resperpi to log data in mysql by using Adfruit and Mysql.connector in python
3. show data by using templete (bootstrap cdn files )
4. profile time taked for insertion and selection in mysql

To log data sensor in database:
```
python Dht11Sensor.py
```

TO run flask api:
```
python app.py
```




## SQLite
1. install sqlite and create table caller (sensor_data)
to install mysql in rasperpi:
```
sudo apt install sqlite3
```
    
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using: 
```
pip install -r requirements.txt
```

3. use resperpi to log data in sqlite3 connector 
4. show data by using templete (bootstrap cdn files and justgang cdn files , matploit for graphing data )
5. profile time taked for insertion and selection in Sqlite 
To Create Sqllite Database:
```
python CreateSqliteDB.py
```
 
To log data sensor in database:
```
python Dht11Sensor.py
```

TO run flask api:
```
python app.py
```


## TinyDB
1. install TinyDB (sensor_data)
2. use resperpi to log data and insert it in tinydb by using DHT11 data (hum , Temp) 
3. show data by using templete (bootstrap cdn files and justgang cdn files , matploit for graphing data )
4. profile time taked for insertion and selection in Sqlite 
