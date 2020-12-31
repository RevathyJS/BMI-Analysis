# -*- coding: utf-8 -*-

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    gender = request.form.getlist("0")
    if  gender[0] == '0':
        int_features_1 = 1
        int_features_2 = 0
    else:
        int_features_1 = 0
        int_features_2 = 1
    
    int_features_3 =int(request.form['2'])
    int_features_4 =int(request.form['3'])
    int_features = [int_features_1,int_features_2,int_features_3,int_features_4]
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Body Mass Index {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)