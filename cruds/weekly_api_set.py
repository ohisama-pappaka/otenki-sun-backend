import requests
import cruds.city_data_file
import config

# 環境変数の定義
API_KEY = config.API_KEY


def weekly_api_set(prefecture_name: str, city_name: str):
    id, city_name = cruds.city_data_file.fetch_city_data(prefecture_name, city_name)
    params = {"units": "metric", "q": city_name, "APPID": API_KEY}
    city_api = "http://api.openweathermap.org/data/2.5/weather"  # 都市名から、座標を求めるAPI
    city_response = requests.get(city_api, params=params)
    city_data = city_response.json()

    lat = city_data["coord"]["lat"]  # 座標獲得
    lon = city_data["coord"]["lon"]  # 座標獲得

    weekly_lat = float(lat)
    weekly_lon = float(lon)
    hourly_params = {"lat": lat, "lon": lon, "units": "metric", "appid": API_KEY}
    weekly_params = {
        "latitude": weekly_lat,
        "longitude": weekly_lon,
        "hourly": ["temperature_2m", "precipitation"],
        "daily": [
            "weathercode",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_hours",
        ],
    }
    hourly_api = "https://api.openweathermap.org/data/2.5/onecall"
    weekly_api = "https://api.open-meteo.com/v1/forecast?timezone=Asia%2FTokyo"

    hourly_response = requests.get(hourly_api, params=hourly_params)
    hourly_weather_data = hourly_response.json()
    weekly_response = requests.get(weekly_api, params=weekly_params)
    weekly_weather_data = weekly_response.json()

    return hourly_weather_data, weekly_weather_data
