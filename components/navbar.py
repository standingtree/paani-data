from dash import html
import dash_bootstrap_components as dbc

def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("State Profiles", href="/state_profiles")),
                dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            ],
            brand="Veles India | Water Data",
            brand_href="/state_profiles",
            color="dark",
            dark=True,
        ),
    ])

    return layout
