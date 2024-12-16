from flask import Flask, render_template, request

app = Flask(__name__)

# This is the main page of the website
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# This is the page the endpoint which calculates the result from the selected state
@app.route('/get_cities')
def get_cities():
    state = request.args.get('state')
    if state == 'CA':
        cities = ['Los Angeles', 'San Francisco', 'San Diego'] 
    elif state == 'NY': 
        cities = ['New York', 'Albany', 'Buffalo']
    return render_template('cities.html', cities=cities)