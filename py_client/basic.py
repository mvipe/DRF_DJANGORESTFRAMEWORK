import requests

endpoint="http://127.0.0.1:8000/"

get_response=requests.get(endpoint) #http requests

print(get_response.text) #print raw text response

print(get_response.json) #it will print json as python dictionary