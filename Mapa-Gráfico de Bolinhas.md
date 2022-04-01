from folium import plugins
from google.colab import files
import plotly.express as px
import folium
import pandas as pd

uploaded = files.upload()

df = pd.read_csv(('covid_19_clean_complete.csv(2)'),parse_dates=['Date'])
df.head(100)

#Otem os dados do último di das bases de dados
temp = df[df['Date'] == max(df['Date'])]

m = folium.Map(location=[0, 0],tiles='cartodbpositron',
                zoom_start=4)#tiles='cartodbpositron'
m.add_child(folium.LatLngPopup())

for i in range(0, len(temp)):
    folium.Circle(
        location=[temp.iloc[i]['Lat'], temp.iloc[i]['Long']],
        color='DarkOrange', fill='DarkOrange',
        tooltip =   '<li><bold>País : '+str(temp.iloc[i]['Country/Region'])+
                    '<li><bold>Confirmados : '+str(temp.iloc[i]['Confirmed'])+
                    '<li><bold>Divisão Regional : '+str(temp.iloc[i]['WHO Region'])+
                    '<li><bold>Mortes : '+str(temp.iloc[i]['Deaths']),
        radius=int(temp.iloc[i]['Confirmed'])/2).add_to(m)
m
