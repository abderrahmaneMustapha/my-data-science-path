#dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#python imports

#my fucntion imports
from graphs import earth,country,big_graph
from data import earth_data,country_data
#static files
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        'crossorigin': 'anonymous'
    }
]

#init the app and server
app = dash.Dash()
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server

#app layout
app.layout = html.Div(children=[
    ####intervals

    ## we need to sperate the countries file update 
    # and citys file update because we are dealing with a large data
    dcc.Interval(
            id='interval-update-countries-csv',
            interval=1*86400000, # one day in milliseconds
    ),
    dcc.Interval(
            id='interval-update-cties-csv',
            interval=1*86600000, #a few minutes more than one day   in milliseconds
    ),

    #hidden div to update my cities csv file because i cant use callback with no output
    html.Div(children=[],style= {'visibility': 'hidden'}, id="cities-csv-update"), 

    ####intervals end
    # earth graph
    html.Div(children=[

        #earth graph
        dcc.Graph(
            id='earth-graph',
            className="col-md-8",
            figure = earth() ,
            config={
        'displayModeBar': False
                }                       
        ),
        #end of earth graph

        #cities for each country
         html.Div(
            
            className="col-md-3 row",
            children=[
                #cities list
            html.H4(children="Algeria Citys", id="citys-title", className="col-12 text-center"),
                html.Ul(children=[
                    html.Li(children=[
                        #add info to the side bar
                        city['location'],
                        #order last
                        html.Div(children=[
                        # data containers
                            html.Div(children=[ 
                                html.P(children="Total",className="small-text"),
                                html.Span(children=city['confirmed'], className="badge badge-warning"),
                            ],  className="ml-1 mr-1 d-flex flex-column align-items-center"),
                            html.Div(children=[
                                html.P(children="Deaths",className="small-text"),
                                html.Span(children=city['dead'], className="badge badge-danger"),
                                ],className="ml-1 mr-1 d-flex flex-column align-items-center"),
                            html.Div(children=[
                                html.P(children="Recovered",className="small-text"), 
                                html.Span(children=city['recovered'], className="badge badge-success")
                            ],className="ml-1 mr-1 d-flex flex-column align-items-center"),
                        #end of data containers                    
                    ], className="d-flex flex-row justify-content-between align-items-center")
                ], className="list-group-item d-flex flex-column justify-content-center align-items-center") for _ , city in country().iterrows()]
                
                ,className="list-group", id="cities-data")
                #end of cities list
            ]
         )
        # end of cities for each country

    ], className="row")  , 
     # end of earth graph  
     #big graph
     html.Div(children=[
         dcc.Graph(
            id='big-graph',
            className="col-md-12",
            figure = big_graph() ,
            config={
        'displayModeBar': False
                }                       
        ),
     ])
     #end big graph
], className="container-fluid")
#end app layout

################# CALL BACKS °°°°°°°°°°°°°°°°°°°°°°°°°°

#update sidbar onclick

#side bar call back start
@app.callback(
    Output('cities-data', 'children'),
    [Input('earth-graph', 'clickData')])
def display_hover_data(clickData):
    name = clickData['points'][0]['customdata'][0] #get country name
    return  [html.Li(children=[
             #add info to the side bar
              city['location'],
              #order last
              html.Div(children=[

                    # data containers
                    html.Div(children=[ 
                        html.P(children="Total", className="small-text"),
                        html.Span(children=city['confirmed'], className="badge badge-warning"),
                    ],className="ml-1 mr-1 d-flex flex-column align-items-center" ),
                    html.Div(children=[
                        html.P(children="Deaths", className="small-text"),
                        html.Span(children=city['dead'], className="badge badge-danger"),
                        ],className="ml-1 mr-1 d-flex flex-column align-items-center"),
                    html.Div(children=[
                        html.P(children="Recovered", className="small-text"), 
                        html.Span(children=city['recovered'], className="badge badge-success")
                    ],className="ml-1 mr-1 d-flex flex-column align-items-center"),
                    #end of data containers
                   
                ], className="d-flex flex-row justify-content-between align-items-center")
              

            ], className="list-group-item d-flex flex-column justify-content-center align-items-center") for _ , city in country(name).iterrows()]
#side bar call back end

#update sidebar title start
@app.callback(
    Output('citys-title', 'children'),
    [Input('earth-graph', 'clickData')])
def update_citys_title(data):

    return  data['points'][0]['location'] + " Citys"
#update sidebar title end

#big line chart  call back start
@app.callback(
    Output('big-graph', 'figure'),
    [Input('earth-graph', 'clickData')]
)
def update_big_line_chart(clickData):
    country = clickData['points'][0]['customdata'][8]
    return big_graph(country=country)
#big line chart  call back end

#interval callback start
#update the map csv file

@app.callback(Output('earth-graph', 'figure'),
              [Input('interval-update-countries-csv', 'n_intervals')])

def update_earth_graph(n):
    return    earth(df=earth_data())

@app.callback(Output('cities-csv-update', 'children'),
              [Input('interval-update-cties-csv', 'n_intervals')])

def update_cities_csv(n):
    country_data()
    return    0
#interval callback end 

if __name__ == '__main__':
    app.run_server(debug=False)