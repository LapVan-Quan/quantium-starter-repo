# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('formatted_sales_data.csv')
print(df)
df = df.sort_values('date')
print(df)

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
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
