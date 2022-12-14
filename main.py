from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
import cruds.city_data_file as city_data_file
import cruds.daily_data_set as daily_data_set
import cruds.hourly_data_set as hourly_data_set
import cruds.weekly_data_set as weekly_data_set


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

favicon_path = "favicon.ico"


@app.get("/")
def root():
    return {"Hello FastAPI!!"}


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)


@app.get("/city/{name}")
def root(name: str):
    main_list = city_data_file.fetch_city_list(name)
    return main_list


@app.get("/daily/{prefecture_name}/{city_name}")  # 毎日の天気予報の出力
def day(prefecture_name: str, city_name: str):
    daily_output_data = daily_data_set.data_set(prefecture_name, city_name)
    return daily_output_data


@app.get("/hourly/{prefecture_name}/{city_name}")  # 毎日の天気予報の出力
def hour(prefecture_name: str, city_name: str):
    hourly_output_data = hourly_data_set.data_set(prefecture_name, city_name)
    return hourly_output_data


@app.get("/weekly/{prefecture_name}/{city_name}")  # 週間の天気予報の出力
def week(prefecture_name: str, city_name: str):
    weekly_output_data = weekly_data_set.data_set(prefecture_name, city_name)
    return weekly_output_data
