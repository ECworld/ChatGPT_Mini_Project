import folium
import pandas as pd
import os
import re
import numpy as np
from folium import plugins

# 해당 폴더에서 전체 파일 찾기
print(os.listdir())

dat = pd.read_csv("Gwangju10_food.csv")
dat.shape

# 데이터 전처리
dat['위도'] = dat['위도'].str.extract('(\d+\.\d+)').astype("float32")
dat['경도'] = dat['경도'].str.extract('(\d+\.\d+)').astype("float32")

# print(df_name.loc[1:5], df_lati.loc[1:5], df_long.loc[1:5] )
dat

df_name = dat['맛집']
df_lati = dat['위도']
df_long = dat['경도']

df_lati

df_lati = list(df_lati)
df_long = list(df_long)
df_loc = np.array([df_lati, df_long]).T

df_loc[0:10]

house_map = folium.Map(location=[ np.mean( df_lati), np.mean(df_long) ], 
                       zoom_start=6)

df_name = list(df_name)
plugins.MarkerCluster(df_loc, popups=df_name).add_to(house_map)

house_map.save(os.path.join('.', 'Gwangju_10food_location.html'))
house_map