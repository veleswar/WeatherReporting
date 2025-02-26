import requests
import json
import Userdetails as user

API_KEY = user.api_key
CITY = 'WELLINGTON'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract_weather_data():
    response = requests.get(URL)
    if response.status_code ==200:
        data=response.json()
        return {
            "city" :data["name"],
            "temperature": data["main"]["temp"],
            "humidity" : data["main"]["humidity"],
            "weather" : data['weather'][0]['description'],
            "timestamp":data['dt']
        }

if __name__ == "__main__":
    print(extract_weather_data())
