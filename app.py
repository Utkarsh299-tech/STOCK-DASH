import dash
from dash import Dash, dcc, html
from datetime import date
from dash.dependencies import Input, Output

# creating app instance
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
  html.Div(
[
html.P("Welcome to the Stock Dash App!", className="start"),
html.Div([
# stock code input
"Input stock code:"
]),
html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='input-button')
]),

html.Div([
# Date range picker input
 dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2030, 9, 19),
        initial_visible_month=date(2030, 8, 5),
        end_date=date(2030, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range')
]),
html.Div([
html.Div([
  # Stock price button
    html.Button('Stock Price', id='btn-nclicks-1', n_clicks=0),
    # Indicators button
    html.Button('Indicators', id='btn-nclicks-2', n_clicks=0),
    html.Div(id='container-button-timestamp')
]),
# Number of days of forecast input
# Forecast button
html.Div([
    html.Div(dcc.Input(id='id-on-forecast', type='text')),
    html.Button('Forecast', id='forecast', n_clicks=0),
    html.Div(id='forecast-button')
]),
]),
],
className="inputs"),

html.Div(
[
html.Div(
[ # Logo
# Company Name
],
className="header"),
html.Div( #Description
id="description", className="decription_ticker"),
html.Div([
# Stock price plot
], id="graphs-content"),
html.Div([
# Indicator plot
], id="main-content"),
html.Div([
# Forecast plot
], id="forecast-content")
],
className="content")

], className="container")

if __name__ == '__main__':
  app.run_server(debug=True)
