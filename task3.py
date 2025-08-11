# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from doctest import OutputChecker
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('formatted_sales_data.csv')
df = df.sort_values('date')

fig = px.line(
    df, 
    x='date', 
    y='sales',
    color='region',
    labels={"date": "Date", "sales": "Sales ($)", "region": "Region"},
    title="Daily Pink Morsels Sales by Region"
)

app.layout = html.Div(children=[
    html.H1("Daily Pink Morsels Sales"),

    dcc.Graph(
        id='my-output',
        figure=fig
    ),

    dcc.RadioItems(
        ['all', 'north', 'south', 'east', 'west'], 
        'all',
        id='my-input',
        inline=True
    )
], style={
    'textAlign': 'center'
})

@callback(
    Output(component_id='my-output', component_property='figure'),
    Input(component_id='my-input', component_property='value')
)
def update_output(input_value):
    if input_value == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == input_value]
    
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales',
        color='region',
        labels={"date": "Date", "sales": "Sales ($)", "region": "Region"},
        title="Daily Pink Morsels Sales by Region"
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
