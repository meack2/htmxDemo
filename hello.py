from flask import Flask, render_template, request
#from wtforms import Form, BooleanField, StringField, validators

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/get_cities')
def get_cities():
    state = request.args.get('state')
    if state == 'CA':
        cities = ['Los Angeles', 'San Francisco', 'San Diego'] 
    elif state == 'NY': 
        cities = ['New York', 'Albany', 'Buffalo']
    return render_template('cities.html', cities=cities)