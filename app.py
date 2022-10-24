import plotly.express as px
import pandas as pd
import geopandas as gpd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
# Connect to app pages
from pages import state_profiles, page2
# Connect data feed
from data_feed import datahelpers as dh
# Connect components
from components import navbar
from components.maps import all_states_geojson


# initialize dash app
app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{"name": "viewport", "content": "width=device-width"}],
           suppress_callback_exceptions=True)

# Define navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])


# Create the callback to handle multipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/state_profiles':
        return state_profiles.layout
    if pathname == '/page2':
        return page2.layout
    else: # if redirected to unknown link
        return "404 Page Error! Please choose a link"


# callback to update state map
@app.callback(
    Output('state-map','figure'),
    Input('chosen-state','data')
)
def update_state_map(selected_state):
    # filter state geometries for selection
    state_geoprops = [_ for _ in all_states_geojson['features'] if selected_state in _['properties']['st_nm']]
    geo_df = gpd.GeoDataFrame.from_features(state_geoprops)  # .merge(df, on="district").set_index("district")
    # print(geo_df.head())
    fig = px.choropleth(geo_df,
                        geojson=geo_df.geometry,
                        locations=geo_df.index,
                        color='st_nm',
                        projection="mercator")
    fig.update_geos(fitbounds="locations", visible=False,
                    resolution=50, scope="asia",
                    showcountries=True, countrycolor="Black",
                    showsubunits=True, subunitcolor="Blue")
    return fig


# callback to update hydrology data
@app.callback(
    Output('state-rainfall', 'figure'),
    Output('state-groundwater', 'figure'),
    Output('state-reservoir', 'figure'),
    Input('chosen-state', 'data'),
)
def update_hydrology(selected_state):
    # filtered rainfall data
    try:
        filtered_rf_data = dh.rf_data.loc[:, selected_state.upper()]
    except KeyError:
        filtered_rf_data = pd.DataFrame(index=dh.rf_data.index)

    rf_fig = px.line(filtered_rf_data)
    rf_fig.update_layout(
        transition_duration=100,
        xaxis_title='Date',
        yaxis_title='millimeter (mm)',
        showlegend=False
    )

    try:
        filtered_gw_data = -dh.gw_data.loc[:, selected_state.upper()].ffill()
    except KeyError:
        filtered_gw_data = pd.DataFrame(index=dh.gw_data.index)
    gw_fig = px.line(filtered_gw_data)
    gw_fig.update_layout(
        transition_duration=100,
        xaxis_title='Date',
        yaxis_title='meters below ground level (mbgl)',
        showlegend=False
    )

    try:
        filtered_res_data = dh.res_data.loc[:, selected_state.upper()]
    except KeyError:
        filtered_res_data = pd.DataFrame(index=dh.res_data.index)
    res_fig = px.line(filtered_res_data)
    res_fig.update_layout(
        transition_duration=100,
        xaxis_title='Date',
        yaxis_title='Billion cu. meters (BCM)',
        showlegend=False
    )

    return rf_fig, gw_fig, res_fig


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
    cities = dh.price_data[dh.price_data['State'] == dh.code_for_state[selected_state]]['City'].unique()
    print(cities)
    try:
        city = cities[0]
    except IndexError:
        city = ''
    return cities, city


@app.callback(
    Output('city-price', 'figure'),
    Input('choose-city', 'value')
)
def update_prices(selected_city):
    # filtered price data
    if selected_city is not None:
        filtered_price_data = dh.price_data[dh.price_data['City'] == selected_city][[
            'City',
            'Price SubType',
            'Monthly Consumption (kL)',
            'Volumetric Rate - USD/acre-ft']
        ]
    else:
        filtered_price_data = dh.price_data[dh.price_data['City'] == 'NA'][[
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

# # chloropleth map -- IN PROGRESS
# @app.callback(
#     Output("graph", "figure"),
#     Input("candidate", "value"))
# def display_choropleth(candidate):
#     df = px.data.election()# replace with your own data source
#     geojson = px.data.election_geojson()
#     fig = px.choropleth(
#         df, geojson=geojson, color=candidate,
#         locations="district", featureidkey="properties.district",
#         projection="mercator", range_color=[0, 6500])
#     fig.update_geos(fitbounds="locations", visible=False)
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#     return fig


if __name__ == '__main__':
    app.run_server(debug=True)
