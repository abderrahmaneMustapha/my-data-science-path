#dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#python imports

#my fucntion imports
from data import earth_data

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
earth_data()
], id="test")


if __name__ == '__main__':
    app.run_server(debug=True)