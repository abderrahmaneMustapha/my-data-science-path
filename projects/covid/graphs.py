#librarys
import json
#plotly and dash
import plotly.express as px

#my python code
from data import open_csv,country_data,search_country_csv

def earth():
    
    df = open_csv("data/countries.csv")
    fig = px.choropleth( df, locations="Country",
                        color="TotalConfirmed", 
                        hover_name="Country", 
                        hover_data=[ 
                            'NewConfirmed','TotalConfirmed',
                            'NewDeaths','TotalDeaths','NewRecovered',
                            'TotalRecovered','Date'
                                   ], 
                        locationmode="country names",
                        projection="orthographic",
                        color_continuous_scale=px.colors.sequential.dense,
                        height=600
                    
                       )
   

    return fig

def countrys(name="dz"):
    cities_list  = search_country_csv(open_csv('data/cities'))
    return cities_list 