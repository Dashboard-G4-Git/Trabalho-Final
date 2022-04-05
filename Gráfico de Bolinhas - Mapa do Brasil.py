import pandas as pd
import plotly.express as px
from folium import plugins
import numpy as np
import folium
import json

df = pd.read_csv(('caso.csv'), parse_dates=['date'])
df.dropna()
df.head(100)

df2 = pd.read_csv('https://raw.githubusercontent.com/sandeco/CanalSandeco/master/covid-19/cidades_brasil.csv')
indexCities = df2.set_index('codigo_ibge')
indexCities.head(100)

cities = df.loc[df.place_type == 'city', :]
cities.place_type.unique()
cities = cities.join(indexCities, on='city_ibge_code')

geo_last = cities.loc[cities.is_last == True, ['date','city', 'latitude', 'longitude', 'state', 'confirmed', 'deaths']]
geo_last = geo_last.dropna(subset=['longitude'])
geo_last = geo_last.dropna(subset=['latitude'])
geo_last.head(100)

m = folium.Map(location=[-9, -50],tiles='Stamen terrain',
                zoom_start=5)#tiles='cartodbpositron' or 'Stamen terrain'
m.add_child(folium.LatLngPopup())

for i in range(0, len(geo_last)):
    folium.Circle(
        location=[geo_last.iloc[i]['latitude'], geo_last.iloc[i]['longitude']],
        color='crimson', fill='crimson',
        tooltip =   '<li><bold>Cidade :       '+str(geo_last.iloc[i]['city'])+
                    '<li><bold>Confirmados :  '+str(geo_last.iloc[i]['confirmed'])+
                    '<li><bold>Regional :     '+str(geo_last.iloc[i]['state'])+
                    '<li><bold>Mortes :       '+str(geo_last.iloc[i]['deaths']),
        radius=int(geo_last.iloc[i]['confirmed'])/3).add_to(m)
m
