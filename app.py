from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.P('Enter a composite number to see its prime factors'),
    dcc.Input(id='num', type='number', debounce=True, min=2, step=1),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])

@app.callback(
    Output('out', 'children'),
    Output('err', 'children'),
    Input('num', 'value'))
def show_factors(num):
    if num is None:
        raise dash.exceptions.PreventUpdate
    
    factors = prime_factors(num)