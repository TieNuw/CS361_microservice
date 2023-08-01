from flask import Flask, request, jsonify
import requests

#name of the app
app = Flask("weather")

#API key, from weatherapi.com
key = "59a65f4774414ef3a85180642232407"


#uses weatherapi.com base url = http://api.weatherapi.com/v1/current
def get_weather(lat, long):
    base_url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{long}'
    response = requests.get(base_url)
    data = response.json()
    return data


@app.route('/weather', methods=['POST',])
def get_coordinates():
    data = request.get_json()

    if 'latitude' not in data or 'longitude' not in data:
        return jsonify({'Error, enter the latitude and longitude.'}), 400

    latitude = data['latitude']
    longitude = data['longitude']

    weather_data = get_weather(latitude, longitude)

    response = {'condition': weather_data['current']['condition']['text']}

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5302)