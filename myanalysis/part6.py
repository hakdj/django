import json

import matplotlib.pyplot as plt
import pandas as pd;
import seaborn as sns;
import folium as fol;
from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES;

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',header=0);

df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl',header=0);

df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=0);
df3.columns= ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];


df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');

df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');
# 경기도 행정 구역


tt = sns.load_dataset('titanic');
# titanic

class Part5:
    def p172(self):
        print(tt.info());



if __name__ == '__main__':
    Part5().p172();