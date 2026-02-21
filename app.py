import os
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request

app = Flask(__name__)
model = load_model('model/model.h5', compile=False)
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
    final_features = np.array([features])

    prediction = np.argmax(model.predict(final_features))
    print(f'features = {features}')
    print(f'final_features = {final_features}')
    print(f'prediction = {prediction}')

    return render_template('predict.html', result=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
