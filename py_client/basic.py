import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

# Application programming interface
# json json={"query": "Hello World"} "content-type": "application/json
# data data={"query": "Hello World"} "content-type": "application/x-www-form-urlencoded"
get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'Hello World'})
print(get_response) 
# print(get_response.text) 

# To run this in command terminal, run the following command in the root directory terminal and type: python py_client/basic.py

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

# print(get_response.json())
# print(get_response.json()['message'])
# print(get_response.status_code)