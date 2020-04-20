import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('cdata.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Advisory.html')