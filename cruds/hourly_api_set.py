import requests
import datetime
import cruds.city_data_file
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ["API_KEY"]


def api_set(prefecture_name: str, city_name: str):
    id, city_name = cruds.city_data_file.fetch_city_data(prefecture_name, city_name)
    params = {"q": city_name, "APPID": API_KEY, "units": "metric"}
    city_api = "http://api.openweathermap.org/data/2.5/weather"  # 都市名から、座標を求めるAPI
    pre_api = f"https://weather.tsukumijima.net/api/forecast/city/{id}"  # 降水確率を求める

    city_response = requests.get(city_api, params=params)
    pre_response = requests.get(pre_api)
    city_data = city_response.json()
    precipitation_json = pre_response.json()

    lat = city_data["coord"]["lat"]  # 座標獲得
    lon = city_data["coord"]["lon"]  # 座標獲得

    hourly_params = {"lat": lat, "lon": lon, "units": "metric", "appid": API_KEY}
    hourly_api = "https://api.openweathermap.org/data/2.5/onecall"
    hourly_response = requests.get(hourly_api, params=hourly_params)
    hourly_json = hourly_response.json()
    date = datetime.datetime.now()

    return precipitation_json, hourly_json, date
