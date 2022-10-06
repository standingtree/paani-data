from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# load long-form dataframe
dataFilepath = 'C:/Users/viren/Documents/___UChicago MSFM/water index'

# rainfall data
rf_data = pd.read_excel(dataFilepath + r'/_consolidated data/actual_rf_all_states.xlsx', index_col=0)

# groundwater data
gw_data = pd.read_excel(dataFilepath + r'/_consolidated data/groundwater_levels_all_states.xlsx', index_col=0)

# reservoir storage data
res_data = pd.read_excel(dataFilepath + r'/_consolidated data/reservoir_storage_all_states.xlsx', index_col=0)

# pricing data
price_data = pd.read_excel(dataFilepath + r'/_consolidated data/consolidated_prices.xlsx')

# codes
state_codes = pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='States',index_col=3)
code_for_state = dict(zip(state_codes['State'], state_codes.index))
basin_codes = pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='RiverBasins',index_col=3)
city_state = dict(pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='CityState',index_col=0))
print(state_codes.head(), basin_codes.head(), city_state)


app = Dash(__name__)

# set up layout elements
# input dropdown: cities
# filter data

app.layout = html.Div([
    html.H1('Veles India | Water Intelligence Platform'),
    html.H2('State Hydrology Data'),
    dcc.Dropdown(
        state_codes['State'].unique(),
        value='Andhra Pradesh',
        id='choose-state'
    ),
    # store choice of state
    dcc.Store(id='chosen-state'),
    html.Div([
        dcc.Graph(id='state-rainfall')
    ],
        style={
            "display": "inline-block",
            "width": "33%"}
    ),
    html.Div([
        dcc.Graph(id='state-groundwater')
    ],
        style={
            "display": "inline-block",
            "width": "33%"}
    ),
    html.Div([
        dcc.Graph(id='state-reservoir'),
    ],
        style={"display": "inline-block",
               "width": "33%"}
    ),
    html.H2('City Water Pricing'),
    dcc.Dropdown(
        price_data[price_data['State'] == 'Andhra Pradesh']['City'].unique(),
        value='Hyderabad',
        id='choose-city'
    ),
    html.Div([
        dcc.Graph(id='city-price'),
    ],
        style={"display": "inline-block",
               "width": "100%"}
    ),

])


@app.callback(
    Output('chosen-state', 'data'),
    Input('choose-state', 'value')
)
def store_chosen_state(selected_state):
    return selected_state


@app.callback(
    Output('choose-city', 'options'),
    Output('choose-city', 'value'),
    Input('chosen-state', 'data')
)
def update_cities(selected_state):
    # cities in selected state for which price data is available
    print(selected_state)
    cities = price_data[price_data['State'] == code_for_state[selected_state]]['City'].unique()
    print(cities)
    try:
        city = cities[0]
    except IndexError:
        city = ''
    return cities, city


# callback to udpate hydrology data
@app.callback(
    Output('state-rainfall', 'figure'),
    Output('state-groundwater', 'figure'),
    Output('state-reservoir', 'figure'),
    Input('chosen-state', 'data'),
)
def update_hydrology(selected_state):
    # filtered rainfall data
    try:
        filtered_rf_data = rf_data.loc[:,selected_state.upper()]
    except KeyError:
        filtered_rf_data = pd.DataFrame(index=rf_data.index)

    rf_fig = px.line(filtered_rf_data)
    rf_fig.update_layout(transition_duration=200, xaxis_title='Date', yaxis_title='Actual Rainfall (mm)')

    try:
        filtered_gw_data = -gw_data.loc[:,selected_state.upper()].ffill()
    except KeyError:
        filtered_gw_data = pd.DataFrame(index=gw_data.index)
    gw_fig = px.line(filtered_gw_data)
    gw_fig.update_layout(transition_duration=200, xaxis_title='Date', yaxis_title='Groundwater Level (mbgl)')

    try:
        filtered_res_data = res_data.loc[:,selected_state.upper()]
    except KeyError:
        filtered_res_data = pd.DataFrame(index=res_data.index)
    res_fig = px.line(filtered_res_data)
    res_fig.update_layout(transition_duration=200, xaxis_title='Date', yaxis_title='Reservoir Storage (BCM)')

    return rf_fig, gw_fig, res_fig


@app.callback(
    Output('city-price', 'figure'),
    Input('choose-city', 'value')
)
def update_prices(selected_city):
    # filtered price data
    if len(selected_city) > 0:
        filtered_price_data = price_data[price_data['City'] == selected_city][[
            'City',
            'Price SubType',
            'Monthly Consumption (kL)',
            'Volumetric Rate - USD/acre-ft']
        ]
    else:
        filtered_price_data = price_data[price_data['City'] == 'NA'][[
            'City',
            'Price SubType',
            'Monthly Consumption (kL)',
            'Volumetric Rate - USD/acre-ft']
        ]

    price_fig = px.scatter(filtered_price_data,
                           x='Monthly Consumption (kL)', y='Volumetric Rate - USD/acre-ft',
                           size='Volumetric Rate - USD/acre-ft',
                           color='Price SubType', hover_name='City',
                           log_x=False)

    price_fig.update_layout(transition_duration=200)

    return price_fig


if __name__ == '__main__':
    app.run_server(debug=True)
