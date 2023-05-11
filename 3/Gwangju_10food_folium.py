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

print(dat)