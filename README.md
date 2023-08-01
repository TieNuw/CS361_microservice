# CS361_microservice

Microservice Communication Contract

This microservice uses Flask using rest API as the primary communication and provides instructions on how to request and receive data.

Requesting data:
An HTTP post is required in order to request data from the microservice. The HTTP post must be requested at the specific endpoint and include the following parameters.

Endpoint: /weather
HTTP Method: POST
parameter = {'latitude': latitude, 'longitude': longitude}

Example of how to make a request:

```
import requests

#get latitude any way you like
latitude = 40
longitude = 50

url = 'http://localhost:5302/weather'
params = {'latitude': latitude, 'longitude': longitude}

response = requests.post(url, json=params)

data = response.json()

print(data) #prints out {'condition': 'Sunny'}
print({data['condition']} #prints out 'Sunny'
```

Important notes: 
-The microservice uses the localhost at port 5302, this can of course be changed as need be.

-Make sure to import requests if using python

-Data comes back as a JSON object. An example of this is {'condition': 'Sunny'}. If you would like to just have the Sunny part of the data. refer to the requested example

UML Diagram:
