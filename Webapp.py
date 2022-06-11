from matplotlib.pyplot import axis
import pandas as pd
from pandas import *
from dash import Dash, dcc, html
import plotly.express as px

col_list = ["Country_code", "Country", "LibrarySize", "No. of TV Shows", "No. of Movies", "CPM_Basic", "CPM_Standard", "CPM_Premium" ]

wholeCSV = pd.read_csv('NetflixFees.csv', usecols=col_list)

df = wholeCSV.reset_index()

netflix_abos = []

for index, row in df.iterrows():
    #Abo-Preis / Library-Size  = Kosten für *eine* einzelne Show/Film
    cost_per_content_basic = (row.CPM_Basic / row.LibrarySize)*100
    cost_per_content_standard = (row.CPM_Standard / row.LibrarySize)*100
    cost_per_content_premium = (row.CPM_Premium / row.LibrarySize)*100

    tmp_list = [row.Country, row.LibrarySize, row.CPM_Basic, row.CPM_Standard, row.CPM_Premium, cost_per_content_basic, cost_per_content_standard, cost_per_content_premium]
    netflix_abos.append(tmp_list)
    
df_new = pd.DataFrame (netflix_abos, columns=["Country", "LibrarySize", "CPM_Basic", "CPM_Standard", "CPM_Premium", "cost_per_content_basic", "cost_per_content_standard", "cost_per_content_premium"])

#Web-Application
app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

fig_basic = px.bar(df_new, x="Country", y="cost_per_content_basic", 
color="CPM_Basic", 
barmode="group")

fig_basic.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    yaxis_title="Cost per *one* Content in Cent with basic subscription",
    xaxis_title="Country",
)

fig_standard = px.bar(df_new, x="Country", y="cost_per_content_standard", 
color="CPM_Standard", 
barmode="group")

fig_standard.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    yaxis_title="Cost per *one* Content in Cent with standard subscription",
    xaxis_title="Country",
)

fig_premium = px.bar(df_new, x="Country", y="cost_per_content_premium", 
color="CPM_Premium", 
barmode="group")

fig_premium.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    yaxis_title="Cost per *one* Content in Cent with premium subscription",
    xaxis_title="Country",
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
    html.H1(
        children='Netflix price-performance ratio in each country',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Cost per Content (Shows, Movies, etc.) for each Country', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='graph_basic',
        figure=fig_basic
    )
]),
 html.Div([
    dcc.Graph(
        id='graph_standard',
        figure=fig_standard
    )
]),
 html.Div([
    dcc.Graph(
        id='graph_premium',
        figure=fig_premium
    )
])
    
])

if __name__ == '__main__':
    app.run_server(debug=True, port=3000)