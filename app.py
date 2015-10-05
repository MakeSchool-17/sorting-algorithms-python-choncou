import os
import csv

from flask import Flask
from flask import render_template

from data_source import DataSource

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

title = "SF GOV Data"

@app.route("/")
def index():
    return render_template('index.html', title=title)

@app.route("/bike_parking")
def bike_parking():
    bp = DataSource('data/Bicycle_Parking__Public_.csv')
    page_title = title + ' : Bike Parking'

    return render_template('table_view.html', title=page_title, headers=bp.headers, rows=bp.rows)

if __name__ == "__main__":
    app.run()
