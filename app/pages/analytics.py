import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our analytics page'),
    html.Div('This is our analytics content')
])