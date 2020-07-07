import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
max_length=110

app = Flask(__name__)
# load model
model = load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    sentences = [str(request.form.values())]
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    output=model.predict(padded)
    
    return render_template('index.html', prediction_text='sarcasm analysis would be: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
