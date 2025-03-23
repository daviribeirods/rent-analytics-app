import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

dash.register_page(__name__, path='/')

# layout = html.Div([
#     html.H1('This is our Home page'),
#     html.Div('This is our Home page content.')
# ])

layout = dbc.Container(
    [   
        # Home page content
        dbc.Row(
            children = [
                # Graph content
                dbc.Col(
                    children = [
                        dcc.Graph()
                    ],
                    width=8
                ),
                # Menu to change graph content
                dbc.Col(
                    children = [
                        html.H2(
                            children = [
                                'Explore the best rental properties in Brasília with RentPrice, powered by AI.'
                            ],
                            className='mt-2'
                        ),
                        html.P(
                            children = [
                                'Brasília is divided administratively into different regions. Select the region to see the houses and apartments by price.'
                            ], 
                            className='mt-4'
                        ),
                                                # Input to select type of property
                        html.P(
                            children = ['Select the type of the property'],
                            style = {
                                'font-weight': 'bold'
                            },
                            className = 'text-bold mt-3'
                        ),
                        dcc.Dropdown(
                            options = [
                                'All',
                                'Apartment',
                                'House'
                            ],
                            value = 'All',
                            placeholder='Select the type of properties'
                        ),
                        # Input to select region
                        html.P(
                            children = ['Select the region in Brasília'],
                            style = {
                                'font-weight': 'bold'
                            },
                            className = 'text-bold mt-3'
                        ),
                        dcc.Dropdown(
                            options = [
                                'Region A',
                                'Region B'
                            ],
                            placeholder='Select the region'
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                children = [
                                    html.H5('Select a region to see properties.'),
                                ],
                                className = 'text-center'
                            ),
                            className = 'mt-4'
                        )
                    ]
                )
            ]
        )
    ],
    fluid=True
)