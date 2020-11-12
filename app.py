from collections import defaultdict

# flask for the web application
import flask as fl
# numpy for the numerical work
import numpy as np

import csv

app = fl.Flask(__name__)

# landing page
@app.route('/')
def index():
    return fl.current_app.send_static_file('index.html')

# api route that returns the csv dataset using numpy
# adapted from https://pythonhealthcare.org/2018/04/04/25-reading-and-writing-csv-files-using-numpy-and-pandas/
@app.route('/api/dataset')
def show_dataset():
    # load in the csv file
    data = np.loadtxt('datasets/powerproduction.csv', delimiter=',', skiprows=1)
    # add the data of the csv to a dictionary
    dictionary = dict(data)
    # return the dictionary
    return dictionary
