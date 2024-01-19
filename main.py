import datetime as dt
import requests 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "7a9974dcb465600a627ef8bfffc130e5"
CITY = "Una"


def kelvin_to_cel(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_cel(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_cel, feels_like_fahrenheit = kelvin_to_cel(feels_like_kelvin)
wind_speed = response['wind']['speed']

humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp( response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp( response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temperature in {CITY} feels like: {feels_like_cel:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/sec")
print(f"Sunrise in {CITY} at {sunrise_time} local time.")
print(f"Sunset in {CITY} at {sunset_time} local time.")

print(f"General Weather in {CITY}: {description}")

