from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash()

app.layout = [
    html.H1(children='Rent Analytics App', style={'textAlign':'center'}),
]

if __name__ == '__main__':
    app.run(debug=True)