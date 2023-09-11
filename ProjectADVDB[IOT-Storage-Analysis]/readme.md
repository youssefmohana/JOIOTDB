#  IOT storage and Anaylsize

1. Use mysql with flask to make iot storage
2. Use Sqllite with flask to make iot storage
3. use TinyDB and Flask (add with caching and without caching)


## MYSQL
1. install mysql (mariiadb for rasperpi lightwieght) and create table caller (Weathe_data) and get code from adufruit (DHT11)

  1. to install mysql in rasperpi:
```
sudo apt install mariadb-server -y
```
  2. run to install all packages 
```
pip install -r requirements.txt
```
2. use resperpi to log data in mysql by using Adfruit and Mysql.connector in python
3. show data by using templete (bootstrap cdn files )
4. profile time taked for insertion and selection in mysql





## SQLite
1. install sqlite and create table caller (sensor_data)
2. use resperpi to log data in sqlite3 connector 
3. show data by using templete (bootstrap cdn files and justgang cdn files , matploit for graphing data )
4. profile time taked for insertion and selection in Sqlite 


## TinyDB
1. install TinyDB (sensor_data)
2. use resperpi to log data and insert it in tinydb by using DHT11 data (hum , Temp) 
3. show data by using templete (bootstrap cdn files and justgang cdn files , matploit for graphing data )
4. profile time taked for insertion and selection in Sqlite 
