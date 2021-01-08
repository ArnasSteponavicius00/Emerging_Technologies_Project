# flask for the web application
from sys import modules
from flask import Flask, request, render_template

# used to load keras model
from tensorflow.keras.models import load_model

# initialize the Flask app
app = Flask(__name__)

def get_model():
    global model
    model = load_model('turbine_model.h5')
    print('model loaded')

# landing page
@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        print('loading keras model')
        get_model()

        speed = request.form['speed']

        prediction = model.predict([float(speed)])

        return render_template('index.html', prediction=prediction[0])
    return render_template('index.html')