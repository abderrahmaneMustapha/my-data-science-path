#librarys
import json
#plotly and dash
import plotly.express as px

#my python code
from data import open_csv,country_data,search_country_csv,get_country_data

def earth(df=open_csv("data/countries.csv")):
    
    fig = px.choropleth( df, locations="Country",
                        color="TotalConfirmed", 
                        hover_name="Country", 
                        hover_data=[ 'CountryCode',
                            'NewConfirmed','TotalConfirmed',
                            'NewDeaths','TotalDeaths','NewRecovered',
                            'TotalRecovered','Date', 'Slug'
                                   ], 
                        locationmode="country names",
                        projection="orthographic",
                        color_continuous_scale=px.colors.sequential.dense,
                        height=600
                    
                       ).update_layout(clickmode='event+select')
   

    return fig

def country(name="dz"):

    cities_list  = search_country_csv(open_csv('data/cities.csv'), name.lower())
    return cities_list.sort_values(by='confirmed', ascending=False)

# return the big line graph figure
def big_graph(country="algeria"):
    return  {
            'data': [
                #confirmed
                {'x': get_country_data(country=country)['Date'], 
                'y': get_country_data(country=country)['Cases'], 
                'type': 'line', 'name': 'Confirmed'},
                #confirmed end

                #deaths 
                 {'x': get_country_data(country=country, statu="deaths")['Date'], 
                'y': get_country_data(country=country, statu="deaths")['Cases'], 
                'type': 'line', 'name': 'Deaths'},
                #deaths end

                #recovered
                {'x': get_country_data(country=country, statu="recovered")['Date'], 
                'y': get_country_data(country=country, statu="recovered")['Cases'], 
                'type': 'line', 'name': 'Recovered'},
                #recovered end
            ],
            'layout': {
                'title': 'All cases From the first recorded case  for '+country
            }
        }