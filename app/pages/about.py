import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/assets/me.jpg",
                        className="img-fluid rounded-start mx-2",
                    ),
                    className="col-md-3 my-5 mx-2",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Davi Santos", className="card-title"),
                            html.P(
                                "I am Davi Santos, a data scientist and solutions engineer with"
                                " a Bachelor's degree in Computer Science from UFT. "
                                " I specialize in data analysis, machine "
                                " learning, and geospatial data, using Python and data visualization "
                                " to extract insights and solve complex problems.",
                                className="card-text text-align-justify",
                                style = {
                                    "textAlign": "justify"
                                }
                            ),
                            html.P(
                                " My curiosity drives me to continuously explore new ways to unlock"
                                " value from data—whether through visualization, predictive modeling,"
                                " or innovative real-world applications.",
                                className="card-text text-align-justify",
                                style = {
                                    "textAlign": "justify"
                                }
                            ),
                            html.Small(
                                "Last updated 2 days ago",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    # style={"maxWidth": "540px"},
)

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
                                """
                                RentPrice Brasília is a data-driven application designed to simplify 
                                the search for rental properties in Brasília. The app provides an 
                                interactive map that allows users to explore available rentals by 
                                region, view property details, and analyze key location-based 
                                statistics."""
                            ]
                        ),
                        html.P(
                            [
                                """
                                    The project was created by me, Davi Santos, as a solution to a 
                                    real challenge I faced — finding the ideal apartment to rent. 
                                    I wanted a place that either had easy access to the subway in 
                                    specific regions or was well-connected with essential amenities 
                                    like supermarkets, gyms, and bus stations. Searching across 
                                    multiple websites and manually comparing options was time-
                                    consuming, so I built RentPrice Brasília to streamline this 
                                    process.
                                """
                            ]
                        ),
                        html.P(
                            [
                                """
                                    The app consists of three main pages:
                                """
                            ]
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    """
                                        Home: An interactive map displaying rental properties, allowing
                                        users to filter by region and view detailed property information.
                                    """
                                ),
                                html.Li(
                                    """
                                        Analytics: A statistical overview of rental trends, including 
                                        insights on proximity to subways, supermarkets, and other key factors.
                                    """
                                ),
                                html.Li(
                                    """
                                        About: This page, where you can learn more about the project and its purpose.
                                    """
                                ),
                            ]
                        ),
                        html.P(
                            [
                                """
                                    Built with Plotly Dash, RentPrice Brasília is a tool designed not just for 
                                    personal use but for anyone looking for a data-driven way to explore rental 
                                    options in Brasília efficiently.
                                """
                            ]
                        )
                    ],
                    className = "mx-2 "
                ),
            ],
            className = 'mx-2 mt-4'
        ),
        dbc.Row(
            dbc.Col(
                    [
                        card
                    ],
                    className = "mx-5"
                )
        )
    ],
    fluid=False    
)