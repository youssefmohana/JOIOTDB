from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import timeit
from tinydb import TinyDB, Query
from flask_caching import Cache
import io
from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)

db = TinyDB('sensor_data.json')
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

sensor_data_table =db.table('sensor_data')


# Retrieve LAST data from database
def getLastData():
    # Retrieve the last data entry from TinyDB
    last_entry = sensor_data_table.all()[-1]

    # Extract temperature, humidity, and timestamp from the last entry
    temp = last_entry.get('temperature')
    hum = last_entry.get('humidity')
    time = last_entry.get('timestamp')
    return time, temp, hum


@cache.cached(timeout=60, key_prefix='getHistData')
def getHistData(numSamples):
    # Retrieve data from TinyDB in descending order of timestamp
    data = sensor_data_table.all()
    data = sorted(data, key=lambda x: x['timestamp'], reverse=True)[:numSamples]

    dates = []
    temps = []
    hums = []

    for row in reversed(data):
        temps.append(row['temperature'])
        hums.append(row['humidity'])
        dates.append(row['timestamp'])

    return dates, temps, hums
print("select data Time:",timeit.timeit(lambda: getHistData(100), number=10))

def maxRowsTable():
    # Retrieve the maximum number of rows from TinyDB
    maxNumberRows = len(sensor_data_table)

    return maxNumberRows
# define and initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
    numSamples = 100
# main route


@app.route("/")
def index():
	time, temp, hum = getLastData()
	templateData = {
	  	'time'	: time,
		'temp'	: temp,
      		'hum'	: hum,
      		'numSamples'	: numSamples
	}
	return render_template('index.html', **templateData)
@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int (request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples-1)
    time, temp, hum = getLastData()
    templateData = {
	  	'time'	: time,
      		'temp'	: temp,
      		'hum'	: hum,
      		'numSamples'	: numSamples
	}
    return render_template('index.html', **templateData)
@app.route('/plot/temp')
def plot_temp():
	times, temps, hums = getHistData(numSamples)
	ys = temps
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Temperature [°C]")
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response
@app.route('/plot/hum')
def plot_hum():
	times, temps, hums = getHistData(numSamples)
	ys = hums
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Humidity [%]")
	axis.set_xlabel("Samples")
	axis.grid(True)
	xs = range(numSamples)
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response
if __name__ == "__main__":
   app.run(host='0.0.0.0',port = 5002, debug=False)
