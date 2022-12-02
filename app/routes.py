# import pickle
# import numpy as np
# from app import app
# from flask import render_template, request

# model = pickle.load(open('app/model/model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     features = [float(x) for x in request.form.values()]
#     final_features = [np.array(features)]
#     prediction = model.predict(final_features)

#     return render_template('index.html', result=prediction[0])
