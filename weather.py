# Author: Martin J Cantu Jr

# The following program will read in locations from the openweather api and store the contents onto a Mongo Database

from pprint import pprint
import requests
from pymongo import MongoClient


def get_temp(arg):
    for items in arg:
        return items['main']


def get_city_name(arg):
    for items in arg:
        return items['name']


def get_country_name(arg):
    for items in arg:
        return items['sys']


def get_weather(arg):
    for items in arg:
        return items['weather']


# The following will insert to the database

def insert_weather():
    try:
        # city_weather = [data]
        db.weather3.insert_one({"city": get_city_name(city_weather)})
        db.weather3.insert_one({"country": get_country_name(city_weather)})
        db.weather3.insert_one({"temp": get_temp(city_weather)})
        db.weather3.insert_one({"weather": get_weather(city_weather)})
        db.weather3.insert_one({"   ": line})
        db.weather3.insert_one({"   ": line})
        print('\nInserted data successfully\n')

    except Exception as e:
        print(str(e))


# The following will read from the database

def read_weather():
    try:
        weatherCol = db.weather3.find()
        print('\nAll the data from Weather Database\n')
        for wea in weatherCol:
            print(wea)

    except Exception as e:
        print(str(e))


# The following will delete from the database depending on which city is used

def delete_weather():
    try:
        db.weather3.delete_one({"city": get_city_name(city_weather)})
        db.weather3.delete_one({"country": get_country_name(city_weather)})
        db.weather3.delete_one({"temp": get_temp(city_weather)})
        db.weather3.delete_one({"weather": get_weather(city_weather)})
        db.weather3.delete_one({"   ": line})
        db.weather3.insert_one({"   ": line})
        print('\nDeletion Successful\n')

    except Exception as e:
        print(str(e))


# This is used to grab the url
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Miami,us&APPID=f8c6d3df2167d332886ce302e5cecded')

data = r.json()  # used to grab the data from the api

client = MongoClient('localhost:27017')  # initialization of client server

db = client.weather3  # initialization of database

city_weather = [data]  # for testing storage

line = "                    "  # used to make space between the locations

# pprint(city_weather)  # for testing


# Execution of Functions (Note: Do not execute all of them at the same time)

# insert_weather()
# read_weather()
# delete_weather()
