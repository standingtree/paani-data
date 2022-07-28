from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# load long-form dataframe
# df = pd.DataFrame(r'C:\Users\viren\Documents\___UChicago MSFM\water index\_consolidated data')
# print(df)

df = pd.DataFrame({
    'Fruit': ['apples', 'oranges', 'bananas', 'apples', 'oranges', 'bananas'],
    'Amount':[10, 11,35,61,1,3],
    'City': ['Bangalore', 'Mumbai', 'Delhi', 'Delhi', 'Hyderabad', 'Chennai']
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode='group')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
    Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='example-graph', figure=fig)
])

if __name__=='__main__':
    app.run_server(debug=True)

