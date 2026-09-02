
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n===== WEATHER =====")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")

    elif response.status_code == 404:
        print("City not found.")

    elif response.status_code == 401:
        print("Invalid API key.")

    else:
        print(f"Error: HTTP {response.status_code}")


city = input("Enter a city: ")

get_weather(city)
