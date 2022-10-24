# Import necessary libraries
from dash import html,dcc
import dash_bootstrap_components as dbc


# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Page 2")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.P("Test page."),
            dbc.Button("Test Button", color="primary"),
            dcc.Graph(id='state-map')
        ]),
        dbc.Col([
            html.P("Column 2."),
        ])
    ])
])