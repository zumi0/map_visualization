from datetime import datetime
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

# read and reshape csv
df_demo = pd.read_csv('data/Japan_earthquakes.csv')
df = df_demo.loc[:,['time','latitude','longitude']]
df.time = pd.to_datetime(df.time, format='%Y-%m-%d %H:%M:%S')
df['hour'] = df.time.apply(lambda x: x.hour)

df_hour = []
for hour in df.hour.sort_values().unique():
    df_hour.append(df.loc[df.hour == hour, ['latitude', 'longitude']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist())

map = folium.Map(location=[df.latitude.mean(), df.longitude.mean()],control_scale=True)
HeatMapWithTime(df_hour, radius=5, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}, min_opacity=0.5, max_opacity=0.8, use_local_extrema=True).add_to(map)
map.save('map/jpn_earthquakes.html')
