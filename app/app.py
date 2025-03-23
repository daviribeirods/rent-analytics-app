import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.COSMO]) # Themes I like: Zephyr, Pulse, Cosmo, Flatly, Sketchy, Journal

app.layout = dbc.Container(
    [
        # First row of the app
        dbc.Row(
            children = [
                # App title
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                html.Div(
                                    children = ['RentPrice Brasília.'],
                                    style = {
                                        'fontSize': 60,
                                    },
                                ),
                                html.Div(
                                    children = [' 2025'],
                                    style = {
                                        'fontSize': 58,
                                        'color': 'red'
                                    },
                                )
                            ],
                            direction = 'horizontal',
                            gap = 5
                        )
                    ]
                ),

                # App buttons links
                dbc.Col(
                    children = [
                        dbc.Button('Home', color='primary', className='mt-4 mx-1', href='/'),
                        dbc.Button('Analytics', color='primary', className='mt-4 mx-1', href='/analytics'),
                        dbc.Button('About', color='primary', className='mt-4 mx-1', href='/about'),
                    ],
                    width=3
                )
            ],
            className = 'mt-4 mx-3' 
        ),
        html.Hr(),

        # content of each page
        dash.page_container
    ],
    fluid=True
)

if __name__ == '__main__':
    app.run(debug=True)