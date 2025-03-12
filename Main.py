from sqlalchemy import create_engine, Integer, Float, Column, select
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlite3
from Class import WeatherData
from tabulate import tabulate

# Creating input lines to use within the class and method calls
latitude = float(input("Enter Latitude: "))
longitude = float(input("Enter Longitude: "))
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))
years = input("Enter years: ").split()


# C3 - Creating an instance of the WeatherData class
weather_info = WeatherData(latitude, longitude, month, day, years)
annual_weather = weather_info.get_weather()
#print(annual_weather)