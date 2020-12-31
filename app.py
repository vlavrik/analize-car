import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from reqs import get_telemetry, convert_unix_ts
import yaml

with open("secrets_private.yaml", 'r') as f:
    secrets_loaded = yaml.safe_load(f)

CREDENTIALS = secrets_loaded['credentials']
DEVICE = CREDENTIALS['device_number']
TOKEN = CREDENTIALS['flespi_token']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

telemetry = get_telemetry(flespi_token=TOKEN, device_number=DEVICE)


app.layout = html.Div([
    html.Article(children=[
        html.Img(id='placeholder',src="https://static01.nyt.com/images/2019/12/23/business/23bmw1/23bmw1-mobileMasterAt3x.jpg", className="car__img"),
        html.Div(children=[html.H2("BMW 316i"),
        html.P(id="km", children=[html.Span("🏎"), ""], className="car__row"),
        html.P(id="fuel",children=[html.Span("⛽️"), ""], className="car__row"),
        html.P(id="temp",children=[html.Span("🌡"), ""], className="car__row"),
        html.P(id="sat",children=[html.Span("🛰"), ""], className="car__row"),
        html.P(id="updt",children=[html.Span("⏱"), ""], className="car__row")

        

        ], className="car__data")





    ], className="car")
    
    
    
    
    
    
    
    
    ],  className='main')

@app.callback(Output(component_id='km', component_property='children'),
Output(component_id='fuel', component_property='children'),
Output(component_id='temp', component_property='children'),
Output(component_id='sat', component_property='children'),
Output(component_id='updt', component_property='children'),

Input(component_id='placeholder', component_property='children'))

def update_output_div(test):
    date = convert_unix_ts(timestamp=telemetry["position.satellites"]["ts"])
    first_comp = [{'props': {'children': '🏎'}, 'type': 'Span', 'namespace': 'dash_html_components'}, '{} km'.format(int(telemetry["vehicle.mileage"]["value"]))]
    second_comp = [{'props': {'children': '⛽️'}, 'type': 'Span', 'namespace': 'dash_html_components'}, '{} l.'.format(telemetry["can.fuel.level"]["value"]*60/100)]
    third_comp = [{'props': {'children': '🌡'}, 'type': 'Span', 'namespace': 'dash_html_components'}, '{} ℃'.format(telemetry["can.ambient.air.temperature"]["value"])]
    fourth_comp = [{'props': {'children': '🛰'}, 'type': 'Span', 'namespace': 'dash_html_components'}, '{}'.format(telemetry["position.satellites"]["value"])]
    firth_comp = [{'props': {'children': '⏱'}, 'type': 'Span', 'namespace': 'dash_html_components'}, '{}'.format(date)]

    return first_comp, second_comp, third_comp, fourth_comp, firth_comp

if __name__ == '__main__':
    app.run_server(debug=False)