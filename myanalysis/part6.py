import json

import matplotlib.pyplot as plt
import pandas as pd;
import seaborn as sns;
import folium as fol;
from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES;

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',header=0);
# 인구이동
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl',header=0);
# 전력량
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=0);
df3.columns= ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];
# auto

df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');

df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');
# 경기도 행정 구역


tt = sns.load_dataset('titanic');
# titanic

class Util:
    def add10(self,n):
        return n+10;
    def add_two(self,a,b):
        return a+b;

class Part6:
    def p218(self):
        df=tt.loc[:,['age','fare']];
        df['ten']=10;
        print(df+100);
        df2= df['age'].apply(Util().add10);
        print(df2);
        df3=df['age'].apply(Util().add_two,b=20);
        print(df3);
        df4=df['age'].apply(lambda x:Util().add10(x));
        print(df4);
        df5=df['age'].apply(lambda x:Util().add_two(20,x));
        print(df5);

if __name__ == '__main__':
    Part6().p218();