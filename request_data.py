import requests
import json



predict_url = 'http://127.0.0.1:5000/predict'

"""fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,
    free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality,Id"""
input = [[4.7, 	0.85, 	0.05, 	1.3, 	0.055, 	13.0, 	78.0, 	0.9924, 	3.56, 	0.82, 	12.9]]

json_ = json.dumps(input)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


input_data = requests.post(in_data_url, data=json_, headers=headers)

print(input, requests.post(in_data_url, data=json_, headers=headers).text)
