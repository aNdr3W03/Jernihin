import os
import numpy as np
from keras.models import load_model
from flask import Flask, render_template, request

app = Flask(__name__)
model = load_model('model/saved_model.h5', compile=False)
model.compile(
    optimizer = 'adam',
    loss      = 'categorical_crossentropy',
    metrics   = ['accuracy']
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    return render_template('predict.html', result=prediction[0])

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
