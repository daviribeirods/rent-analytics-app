import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container(
    [
        # Title of About page
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1('About the project')
                    ]
                )
            ],
            className = 'mx-2',
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                'This project is written and developed by Davi Santos. Davi Santos is a data scientist, data analyst and Bachelor in Computer Science from UFT.'
                                'This project intended to solver Davi\'s personal idea for searching a new apartament to live. Daily, he used to visit different websites'
                                'search for a new rental property. And that\'s when he came up with this idea: gathering in one place information about rental properties'
                                'and to some analysis.'
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    [
                        'This is another column'
                    ]
                )
            ],
            className = 'mx-2 mt-4'
        )
    ],
    fluid=True    
)