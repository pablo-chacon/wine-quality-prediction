from flask import Flask, request, jsonify, redirect, url_for
import json
import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def prediction():
	data = request.get_json()
	input_prediction  = np.array2string(model.predict(data))

	return jsonify(input_prediction)



if __name__ ==" __main__":
	
	in_data = pickle.load(open("model.pkl", "rb"))

	print(model.summary())


	app.run(debug=True, host='0.0.0.0')