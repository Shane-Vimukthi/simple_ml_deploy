import json
import requests


url = ' http://127.0.0.1:8001/model'


request_data = json.dumps({'age': 46, 'salary': 4000})
response = requests.post(url, request_data)

print(response.text)