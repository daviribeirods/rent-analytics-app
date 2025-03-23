import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # main app framework
        dbc.Row(
            [
                html.Div(
                    children = ['Brasilia Rent Analytics App'],
                    style = {
                        'fontSize': 50,
                        'textAlign': 'center'
                    }
                )
            ]
        ),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run(debug=True)