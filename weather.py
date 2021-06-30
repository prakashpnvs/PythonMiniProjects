import json
import os
import geocoder
import requests

from dotenv import load_dotenv

load_dotenv()


def get_current_location():
    g = geocoder.ip('me')
    return g.latlng


def get_current_weather_data(lat, lng):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    querystring = {"lat": lat, "lon": lng,
                   "appid": os.getenv("APP_ID"), "units": "imperial"}
    response = requests.request("GET", url, params=querystring)
    return json.dumps(json.loads(response.text), indent=2)


if __name__ == '__main__':
    latlng = get_current_location()
    print(get_current_weather_data(latlng[0], latlng[1]))
