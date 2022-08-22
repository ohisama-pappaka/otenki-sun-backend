import datetime
import cruds.dailynhourly_api_set as dailynhourly_api_set
import cruds.day_precipitation as day_precipitation


def data_set(prefecture_name: str, city_name: str):
    precipitation_data, hourly_input_data, date = dailynhourly_api_set.api_set(
        prefecture_name, city_name
    )

    day_data = datetime.date.today()
    time = f"{day_data.month}/{day_data.day}"  # 日付
    hours = f"{time}/{date.hour % 24 }:00"  # 時間
    weather = hourly_input_data["hourly"][0]["weather"][0]["icon"]  # 天気情報
    temperature = round(hourly_input_data["hourly"][0]["temp"])  #  気温
    humidity = hourly_input_data["hourly"][0]["humidity"]  # 湿度
    extra_time = date.hour
    pre = day_precipitation.day_precipitation(extra_time, 0, precipitation_data)  # 降水確率

    icon_url = f"http://openweathermap.org/img/w/{weather}.png"

    # 日付、時刻（時のみ）、天候のアイコンURL、気温、湿度、降水確率で出力
    output_data = {
        "time": time,
        "hour": hours,
        "icon_url": icon_url,
        "temperature": temperature,
        "humidity": humidity,
        "precipitation": pre,
    }

    return output_data
