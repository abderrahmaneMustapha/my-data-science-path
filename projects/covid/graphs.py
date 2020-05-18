#librarys
import json
#plotly and dash
import plotly.express as px

#my python code
from data import open_csv

def earth():
    
    df = open_csv("data/countries.csv")
    fig = px.choropleth( df, locations="Country",
                        color="TotalConfirmed", 
                        hover_name="Country", 
                        locationmode="country names",
                        projection="orthographic",
                        color_continuous_scale=px.colors.sequential.OrRd
                       )
   

    return fig