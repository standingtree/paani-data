# Import necessary libraries
from dash import dcc, html
import dash_bootstrap_components as dbc
from datahelpers import data_feed as dh

stateSelector = [
        html.Hr(),
        html.Center(html.H2("State Hydrology Data")),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            dh.state_codes['State'].unique(),
            value='Andhra Pradesh',
            id='choose-state'),
        html.Br(),
        html.Br(),
    ]

selectedStateMap = [
    dbc.Col([
        html.Center(html.H6("State Map")),
        dcc.Graph(id='state-map')
    ]),
]

hydrologyCharts = [
    dbc.Col([
        html.Center(html.H6("Historical Rainfall (mm)")),
        dcc.Graph(id='state-rainfall')
    ]),
    dbc.Col([
        html.Center(html.H6("Groundwater Level (-mbgl)")),
        dcc.Graph(id='state-groundwater')
    ]),
    dbc.Col([
        html.Center(html.H6("Reservoir Storage (BCM)")),
        dcc.Graph(id='state-reservoir')
    ]),
    html.Br(),
    html.Br(),
]

citySelector = [
    html.Hr(),
    html.Center(html.H2("City Water Pricing")),
    html.Br(),
    html.Br(),
    dbc.Col([
        dcc.Dropdown(
        dh.price_data[dh.price_data['State'] == 'Andhra Pradesh']['City'].unique(),
        value='Hyderabad',
        id='choose-city'
        )]),
    html.Br(),
    html.Br(),
]

#
cityPriceChart = [
    dbc.Col([
        dcc.Graph(id='city-price')
    ]),
    html.Br(),
    html.Br(),
]


waterStressScore = [
    html.Hr(),
    html.Center(html.H2("Water Stress Score")),
    html.Br(),
    html.Br(),
    dbc.Col([
        dcc.Graph(id='water-stress-score')
    ]),
    html.Br(),
    html.Br(),
]



# Define the page layout
layout = dbc.Container([
    # store choice of state
    dcc.Store(id='chosen-state'),
    # rows of content
    dbc.Row(stateSelector),
    dbc.Row(selectedStateMap),
    dbc.Row(hydrologyCharts),
    dbc.Row(citySelector),
    dbc.Row(cityPriceChart),
    dbc.Row(waterStressScore)

])





