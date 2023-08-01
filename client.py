import requests

def main():
    while True:

        #getting an input from a user
        latitude = input("Enter latitude: ")
        longitude = input("Enter longitude: ")

        #sending the request over to the service
        url = 'http://localhost:5302/weather'
        params = {'latitude': latitude, 'longitude': longitude}

        #printing the information out
        response = requests.post(url, json=params)
        data = response.json()
        print(data)
        print(f"Current weather at location is {data['condition']}")


if __name__ == "__main__":
    main()