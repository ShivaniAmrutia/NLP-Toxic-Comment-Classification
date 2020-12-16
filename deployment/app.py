import numpy as np, pandas as pd
import tensorflow as tf 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)