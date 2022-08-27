import time

from requests import *
from json import *


while True:
    city_name=input("Please Enter a City Name: ")
    API_key="7ac37f2a5048b1859fdc4e59eb39b602"
    language="tr"
    unit="metric"

    weather_url=f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang={language}&units={unit}"
    content=get(weather_url).json()

    country=content["sys"]["country"]
    current_weather=content["weather"][0]["description"]
    temperature=content["main"]["temp"]
    feels=content["main"]["feels_like"]
    temp_max=content["main"]["temp_max"]
    temp_min=content["main"]["temp_min"]
    pres=content["main"]["pressure"]
    humidity=content["main"]["humidity"]
    now=time.localtime()

    print(time.asctime(now))
    time.sleep(1)
    print(f"                Weather information for {city_name.upper()}:\n\nThe Weather: {current_weather.upper()}\nTemperature: {temperature}°\nFeels Like: {feels}°\nHumidity: {humidity}%\nMaximum Temperature: {temp_max}°\nMinimum Temperature: {temp_min}°\nPressure: {pres} mb")

    




