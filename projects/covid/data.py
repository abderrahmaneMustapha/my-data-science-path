##### get data from the API
import requests
def earth_data():
    
    data = requests.get('https://api.covid19api.com/summary')
    print(data['Global'])
    return data
