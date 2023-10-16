from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')

def task5():
    today = datetime.today()
    days_to_saturday = (5 - today.weekday()) % 7
    return f"There are {days_to_saturday} days left to the nearest Saturday."
