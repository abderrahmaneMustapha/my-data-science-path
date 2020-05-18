#dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#python imports

#my fucntion imports
from graphs import earth 

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
#server = app.server

#app layout
app.layout = html.Div(children=[
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
            id='country-graph',
            className="col-md-3",
            children=[
                #cities list
                html.Ul(children=[])
                #end of cities list
            ]
         )
        # end of cities for each country

    ], className="row")   
     # end of earth graph  
], className="container-fluid")
#end app layout



if __name__ == '__main__':
    app.run_server(debug=True)