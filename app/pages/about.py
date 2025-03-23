import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is the about page'),
    html.Div('This is the about page content')
])