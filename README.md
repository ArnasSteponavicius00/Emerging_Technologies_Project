# Predicting Wind Turbine power output based on wind speed


## Introduction
Project for Emerging Technologies - 4th Year. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values. The dataset used to train the model was provided in a csv format.


* Have Python 3.8 installed on your machine
* Install [Tensorflow](https://www.tensorflow.org/)
    - ```conda install -c anaconda tensorflow```
    <br/>
    **OR**
    - ```pip install tensorflow```
* (Optional) Install [Jupyter Notebook](https://jupyter.org/) if you wish to modify the "training_model.ipynb" file.
    - ```conda install -c conda-forge notebook```
    <br/>
    **OR**
    - ```pip install notebook```

Clone the repository  
```
https://github.com/ArnasSteponavicius00/Emerging_Technologies_Project.git
```
* Open command terminal inside the cloned directory
* Run the following commands:
```
pip install -r requirements.txt
```
This will install all the required packages to run the project.
If you wish to run the application you can use the following commands in the terminal:
<br /> 
**Unix Bash (Linux, Mac, etc):**
```
export FLASK_APP=app.py
flask run
```
**Windows CMD:**
```
set FLASK_APP=app.py
flask run
```
## Jupyter Notebook
Jupyter Notebook can be used to modify the "training_model.ipynb" file, just open the terminal inside the repository directory and run:
```
jupyter notebook
```

## Docker
If [Docker](https://www.docker.com/) is installed, the application can be built and run using:
```
docker build -t [container-name] .
```
To run the docker container:
```
docker run -d -p 5000:5000 [container-name]
```
The application should now be running on http://127.0.0.1:5000/


## Contents:
#### Jupyter Notebook
The Jupyter Notebook trains a neural network to predict the power output of a wind turbine based on wind speed values. The neural network trains on a dataset that has 2 columns (speed, power). The dataset can be viewed in the datasets folder. It showcases to different networks: 
1. A network using linear activation function and one neuron
2. A network with multiple hidden layers using a ReLU activation function then using a linear activation on the final neuron to fit the prediction.

#### Flask Application
The flask application uses the trained model that is saved from the Jupyter notebook to create an application that can be used to input speed values into an input box and then display the predicted power output for that speed value.
**Can be deployed using Docker**.

## Author:
* Arnas Steponavicius

## References:
* [Ian McLoughlin](https://github.com/ianmcloughlin)

