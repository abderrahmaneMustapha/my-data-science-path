##### get data from the API
import pandas as pd
import json

import requests

def earth_data():   

    data = requests.get('https://api.covid19api.com/summary')
    countries = pd.DataFrame(data.json()['Countries'])
    countries.to_csv('data/countries.csv', sep=',', )
    return countries

def open_csv(file_path):
    result = pd.read_csv(file_path)

    return result
    
