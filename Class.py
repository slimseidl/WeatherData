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
