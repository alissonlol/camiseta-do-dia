from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('calendar.json', 'r') as calendar:
        tshirt = json.load(calendar)

    if tshirt['verde']:
        color = 'verde'
    else:
        color = 'roxa'
    return render_template('index.html', data=color)
