import plotly.express as px
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import plotly.offline as py

#Elementos Gráficos do DASH
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True)


#Data Frames//
df = pd.read_csv(r"C:\Users\João Pedro\OneDrive\Documentos\Estevão FIC\Faculdade UnB\CIC0004 - APC\Testes Python\DASH\DASHTEST_ORIGINAL2\WHO-COVID-19-global-data.csv")
df_2 = df[df['Country_code']=='BR']
covid_df = pd.read_csv ('https://raw.githubusercontent.com/bcmths/COVID19/main/global-data.csv')
br_covid_df = covid_df[covid_df['Country_code'] == 'BR']
df_3 = pd.read_csv(r"C:\Users\João Pedro\OneDrive\Documentos\Estevão FIC\Faculdade UnB\CIC0004 - APC\Testes Python\DASH\DASHTEST_ORIGINAL2\covid_grouped.csv")

#Colors//
colors = {
    'background': '#111111',
    'text': 'blueviolet'
}

#Graphics//
cumulativesCases = px.area(df_2,
    x = 'Date_reported', y = 'Cumulative_cases', color_discrete_sequence=["blueviolet"],
    labels={'Date_reported':'Data', 'Cumulative_cases':'Casos Cumulativos'},
)
pieDeaths = px.pie(df,
              values='Cumulative_deaths',
              names='Country'
)
newCases = px.bar(br_covid_df, color_discrete_sequence=["blueviolet"],
  x = 'Date_reported', y = 'New_cases',
  labels={'Date_reported':'Data', 'New_cases':'Novos Casos'}
)
newDeaths = px.bar(br_covid_df, color_discrete_sequence=["blueviolet"],
  x = 'Date_reported', y = 'New_deaths',
  labels={'Date_reported':'Data', 'New_deaths':'Novas Mortes'}
)
pieCases = px.pie(df,
             values='Cumulative_cases',
             names='Country')
cumulativesDeaths = px.area(df_2,
    x = 'Date_reported', y = 'Cumulative_deaths', color_discrete_sequence=["blueviolet"],
    labels={'Date_reported':'Data', 'Cumulative_deaths':'Mortes Cumulativas'},
)

#Gráfico Mapa
epicentros = px.scatter_geo(df_3,
                      locations="iso_alpha",
                      size="Deaths",
                      size_max=75,
                      hover_name="Country/Region",
                      color_continuous_scale="ice",
                      animation_frame="Date",
                      width=2500,
                      height=720,
                      template='plotly_dark',
                      labels={'Date': 'Data', 'iso_alpha':'Sigla de país', 'Deaths':'Mortes'}
)
#Atualizando as cores dos gráficos
cumulativesCases.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
pieDeaths.update_traces(
    textposition='inside',
    textinfo='percent+label'
)
pieDeaths.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    uniformtext_minsize=12,
    uniformtext_mode='hide'
)
newCases.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
newDeaths.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
pieCases.update_traces(
    textposition='inside',
    textinfo='percent+label'
)
pieCases.update_layout(
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
cumulativesDeaths.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

epicentros.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

#Dashboard
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[#div master
html.H1('COVID-19', style={'textAlign': 'center', 'color': colors['text']}),#propriedades da div
     html.P('Dados Sobre COVID-19', style={'textAlign': 'center', 'color': colors['text']}),
     
html.Div(children=[     
        html.Div(children=[  
        html.H2('Mapa dos epicentros da doença', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure= epicentros),
]),
],style={'display':'flex','justify-contente':'center'}),
#divisão "master"
html.Div(className='row', children=[#pai das funçoes a baixo
     html.Div(className='four columns div-user-controls', children=[
        html.H2('Mortes cumulativas', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=cumulativesDeaths),
        ]),
html.Div(className='row', children=[
     html.Div(className='four columns div-user-controls', children=[
        html.H2('Novos Casos', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=newCases)
        ]),
html.Div(className='row', children=[
    html.Div(className='four columns div-user-controls', children=[
        html.H2('Novas Mortes', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=newDeaths)
        ]),
html.Div(className='row', children=[
    html.Div(className='four columns div-user-controls', children=[
        html.H2('Casos cumulativos', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=cumulativesCases)]),
html.Div(className='row', children=[
    html.Div(className='four columns div-user-controls', children=[
        html.H2('Concentração de Casos', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=pieDeaths)]),
html.Div(className='row', children=[
    html.Div(className='four columns div-user-controls', children=[
        html.H2('Concentração de Mortes', style={'textAlign': 'center', 'color': colors['text']}),
                dcc.Graph(figure=pieCases)]),
        ]),
        ]),
        ]),
        ]),
    ]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)