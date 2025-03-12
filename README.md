# Weather Data Python Application

# Overview
This project obtains data from the Open-Meteo Weather API using values from user input. These values include latitude, longitude, specific day and month, and a range of years separated by a space. The data retrieved from the API is then stored in a database using SQLite & SQLAlchemy and queried to retrieve the data in a presentable format using tabulate.

# Files
- Class.py defines the WeatherData class, method to retrieve data from open-meteo, and methods for retrieving weather variables.
- Main.py creates an instance of the WeatherData class, connects to a SQLite database, creates a table, inserts data into the table, and then queries the table.
- Test.py imports the unittest module and defines methods for setting up the test with common attributes to eliminate redundancy between tests. Testing methods are also defined.

# Requirements
- Requests Module
- SQLAlchemy
- SQLite
- Tabulate
- Unittest
- User Input of latitude, longitude, day, month, years to iterate over separated by a space
