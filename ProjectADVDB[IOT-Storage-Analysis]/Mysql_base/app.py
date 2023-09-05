from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import  mysql.connector as  con
import time 
# create   flask object for make routtes  to apis  
app = Flask(__name__)



# Mysql Configration
db_config =  {
    'user': 'root',
    'password': 'Jo123',
    'host': 'localhost',
    'database':'Wearher_db',
    }


def performace_Anaylsize(times):
    f = open("Query Analysize", "w")
    f.write(times)
    f.close()

 
@app.route('/')
def index():
    #connect to Mysql
    db_connnection=  con.connect(**db_config)
    db_cursor= db_connnection.cursor()
    
    #Retrive data
    start_time = time.time()
    db_cursor.execute("SELECT * FROM WEATHER_data ")
    data = db_cursor.fetchall()
    end_time = time.time()
    performace_Anaylsize(  'retrive time '+ str(end_time - start_time))
    # Extract data for plotting the graph
    timestamps = [row[3] for row in data]
    temperatures = [row[1] for row in data]
    humidities = [row[2] for row in data]

    # Generate the graph
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label='Temperature (°C)')
    plt.plot(timestamps, humidities, label='Humidity (%)')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Temperature and Humidity Data')
    plt.legend()

    # Save the graph to a BytesIO object
    graph = BytesIO()
    plt.savefig(graph, format='png')
    graph.seek(0)
    graph_url = base64.b64encode(graph.getvalue()).decode()


    
    #close Connection
    db_cursor.close()
    db_connnection.close()

    return render_template('index.html', data=data, graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug = True , host ='0.0.0.0')