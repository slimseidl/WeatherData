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

# Defining a method to query the weather data from the Weather table

def query_weather(latitude, longitude, month, day, years):

    # Connecting to the database
    conn = sqlite3.connect('weather.db')
    # Creating a cursor object to use SQL commands
    cursor = conn.cursor()
    # Converting years to a comma separated string to query records from multiple years
    years_str = ",".join(years)

    query = f"""Select * From Weather Where latitude = {latitude} and longitude = {longitude} and month = {month} and day = {day} and years in ({years_str})"""

    cursor.execute(query)
    # Retrieving all rows from the query
    results = cursor.fetchall()


    if results:
        # If there are results, column names correspond to fields in the database
        columns = ("Month", "Day", "Year", "Mean Temperature", "Min Temperature", "Max Temperature", "Mean Wind","Min Wind", "Max Wind", "Total Precipitation", "Min Precipitation", "Max Precipitation")

        # Using a loop to iterate through the rows, storing the rows in a dictionary where the result's index matches the column order of the database
        pretty_results = []
        for result in results:
            pretty_result = {
                "Month": result[3],
                "Day": result[4],
                "Year": result[5],
                "Mean Temperature": result[6],
                "Min Temperature": result[7],
                "Max Temperature": result[8],
                "Mean Wind": result[9],
                "Min Wind": result[10],
                "Max Wind": result[11],
                "Total Precipitation": result[12],
                "Min Precipitation": result[13],
                "Max Precipitation": result[14]
            }
            pretty_results.append(pretty_result)
        # Pretty Printing / Formatting Table to make it more readable
        # Headers value means the keys from the dictionary are used as column headers
        # Fancy grid uses a fancy table style
        print(tabulate(pretty_results, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No results found.")

    # Closing the cursor and connection
    cursor.close()
    conn.close()

#Querying the weather
query_weather(latitude, longitude, month, day, years)