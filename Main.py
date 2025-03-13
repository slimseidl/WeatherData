from sqlalchemy import create_engine, Integer, Float, Column, select
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlite3
from Class import Weather
from tabulate import tabulate

# Creating input lines to use within the class and method calls
latitude = float(input("Enter Latitude: "))
longitude = float(input("Enter Longitude: "))
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))
years = input("Enter years: ").split()


# Creating an instance of the WeatherData class
weather_info = Weather(latitude, longitude, month, day, years)
annual_weather = weather_info.get_weather()
#print(annual_weather)

base = declarative_base()

# Creating a table using SQLite and SQLAlchemy

#Creating second class with attributes that represent columns in the SQLite table
class WeatherTable(base):
    __tablename__ = 'Weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    years = Column(Integer, nullable=False)
    mean_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    mean_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)
    total_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

#Creating the database
engine = create_engine('sqlite:///weather.db')
base.metadata.drop_all(engine)
base.metadata.create_all(engine)

#Creating a session to interact with data and database
Session = sessionmaker(bind=engine)
session = Session()

#Using a loop to insert data into the table
for annual in annual_weather:
    record = WeatherTable(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        years=annual['year'],
        mean_temp=annual.get('mean_temp'),
        min_temp=annual.get('mean_temp'),
        max_temp=annual.get('mean_temp'),
        mean_wind=annual.get('max_wind'),
        min_wind=annual.get('max_wind'),
        max_wind=annual.get('max_wind'),
        total_precipitation=annual.get('precipitation'),
        min_precipitation=annual.get('precipitation'),
        max_precipitation=annual.get('precipitation'),
    )
    session.add(record)

session.commit()
session.close()

