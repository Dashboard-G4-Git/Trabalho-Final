import plotly.express as px
from dash import Dash, html, dcc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = Dash(__name__)

#Data Frames//
df = pd.read_csv(r'D:\Downloads\WHO-COVID-19-global-data.csv')
df_2 = df[df['Country_code']=='BR']
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

#Colors//
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Graphics//
fig = px.area(df_2,
    x = 'Date_reported', y = 'Cumulative_cases',
    labels={'Date_reported':'Data', 'Cumulative_cases':'Casos Cumulativos'},
    title='Casos Cumulativos de COVID-19'
    
    )
fig2= px.histogram(df_2, x = 'Date_reported', y = 'New_cases',
    title='Number of Cases from covid by year',
    labels={'Date_reported':'Date', 'New_cases':'Cases by month'
})
fig2.update_traces(xbins_size = 'M1')
fig2.update_layout(bargap=0.1)
fig2.update_xaxes(showgrid=True, ticklabelmode='period', dtick = 'M1', tickformat='%b\n%Y')

fig3 = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
    color_discrete_sequence=["fuchsia"], zoom=3, height=400
)
fig3.update_layout(mapbox_style="open-street-map")
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Update Layout//
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

#Dashboard
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('COVID-19', style={'textAlign': 'center', 'color': colors['text']}),    
    html.P('Dados Sobre COVID-19', style={'textAlign': 'center', 'color': colors['text']}),
    
    html.H2('CASOS CUMULATIVOS', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(figure=fig),

    html.H2('NUMERO DE CASOS POR ANO DE COVID-19', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(figure=fig2),

    html.H2('EPICENTROS DA EPIDEMIA', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(figure= fig3),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)