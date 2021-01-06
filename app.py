# flask for the web application
from sys import modules
import flask as fl
# numpy for the numerical work
import numpy as np
# used to load keras model
from tensorflow.keras.models import Sequential, save_model, load_model

# initialize the Flask app
app = fl.Flask(__name__)

def get_model():
    global model
    model = load_model('turbine_model.h5')
    print('model loaded')

# landing page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# api route that returns the csv dataset using numpy
# adapted from https://pythonhealthcare.org/2018/04/04/25-reading-and-writing-csv-files-using-numpy-and-pandas/
@app.route('/predict', methods=['POST'])
def predict():
    print('loading keras model')
    get_model()

    message = fl.request.get_json(force=True)
    speed = message['speed']

    prediction = model.predict([float(speed)]).tolist()

    response = {
        'prediction': { 
            'power': prediction[0]
        }
    }

    print(response)
    return fl.jsonify(response)