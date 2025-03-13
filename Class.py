import requests
import json


# Creating class Weather
class Weather:
    def __init__(self, latitude, longitude, day, month, years):
        self.latitude = latitude
        self.longitude = longitude
        self.day = day
        self.month = month
        self.years = years
        self.mean_temperature = None
        self.max_wind = None

        # Defining a method to call API from open-meteo and return weather data for location

    def get_weather(self):
        yearly = []
        # Looping through the years
        for year in self.years:
            url = (f'https://archive-api.open-meteo.com/v1/archive?'
                   f'&latitude={self.latitude}&longitude={self.longitude}'
                   f'&start_date={year}-{self.month:02d}-{self.day:02d}&end_date={year}-{self.month:02d}-{self.day:02d}'
                   f'&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max'
                   f'&temperature_unit=fahrenheit'
                   f'&wind_speed_unit=mph'
                   f'&precipitation_unit=inch')
            response = requests.get(url)

            # Branching to determine if data is retrieved successfully or failed

            if response.status_code == 200:
                weather_data = response.json()

                # Dictionary to hold data from API

                daily = {
                    "year": year,
                    "mean_temp": weather_data["daily"]["temperature_2m_mean"][0],
                    "max_wind": weather_data["daily"]["wind_speed_10m_max"][0],
                    "precipitation": weather_data["daily"]["precipitation_sum"][0]
                }
                yearly.append(daily)
            else:
                print(f"Could not retrieve weather data with response code: {response.status_code}")
        return yearly

    # adir = WeatherData(43.764, -73.7585, 2, 10, range(2020,2025))
    # print(f'Average temperature for Adirondack, NY on October 2nd, 2020: {adir.get_weather()[0]["mean_temp"]}')

    # Defining methods for obtaining weather variables and returning list of tuples with the year and value for method
    def get_mean_temp(self):
        weather_info = self.get_weather()
        return [(yearly["year"], yearly["mean_temp"]) for yearly in weather_info]

    def get_max_wind(self):
        weather_info = self.get_weather()
        return [(yearly["year"], yearly["max_wind"]) for yearly in weather_info]

    def get_sum_precip(self):
        weather_info = self.get_weather()
        return [(yearly["year"], yearly["precipitation"]) for yearly in weather_info]

# Calling methods to test
# adir = WeatherData(43.764, -73.7585, 2, 10, range(2020,2025))
# print(f'Average temp for Adirondack, NY on October 2nd in year range:', adir.get_mean_temp())
# print(f'Max wind speed for Adirondack, NY on October 2nd in year range:', adir.get_max_wind())
# print(f'Total precipitation for Adirondack, NY on October 2nd in year range:', adir.get_sum_precip())