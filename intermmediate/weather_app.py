import requests
city = input("Enter city name:")

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    'name': city,
    'count': 1,
    'language': 'en',
    'format':'json'
}
try:
    response = requests.get(url, params=params)
except requests.RequestExcception:
    print("Unable to connect to the weather service.")
    exit()

data = response.json()

if "results" not in data:
    print("City not found!!")
    exit()

latitude = data['results'][0]['latitude']
longitude = data['results'][0]['longitude']

weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

try:
    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )
except requests.RequestException:
    print("Unable to connect to the weather service.")
    exit()

weather_data = weather_response.json()

if "current" not in weather_data:
    print("Invalid response received from the weather service.")
    exit()

temperature = weather_data["current"]["temperature_2m"]
humidity = weather_data["current"]["relative_humidity_2m"]
wind_speed = weather_data["current"]["wind_speed_10m"]

print("\n",city,"Weather Information")
print("------------------------------")
print("temperature =",temperature,"%C")
print("Humidity =",humidity, "%")
print("WInd Speed =", wind_speed,"km/h")
print("------------------------------")