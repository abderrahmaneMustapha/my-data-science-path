##### get data from the API
import pandas as pd
import json

import requests

def earth_data():   

    data = requests.get('https://api.covid19api.com/summary')
    countries = pd.DataFrame(data.json()['Countries'])
    countries.to_csv('data/countries.csv', sep=',', )
    return countries

def country_data():
    data = requests.get('https://www.trackcorona.live/api/cities')
    provinces = pd.DataFrame(data.json()['data'])
    provinces.to_csv('data/cities.csv', sep=',', )
    return provinces

def open_csv(file_path):
    result = pd.read_csv(file_path)

    return result

def search_country_csv(data,query):
   

    return data.query('country_code =='+query)



    
