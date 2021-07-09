import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd;
import seaborn as sns;
import folium as fol;
from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES;

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',header=0);

df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl',header=0);

df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=0);
df3.columns= ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];
# 자동차 데이터

df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');

df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');
# 경기도 행정 구역


tt = sns.load_dataset('titanic');
# titanic

class Part5:
    def p172(self):
        print(tt.info());
        print(tt['deck'].value_counts(dropna=False));
        print(tt.isnull().sum());
        tt1=tt.dropna(axis=1,thresh=500);
        print(tt1.isnull().sum());
        ttage = tt.dropna(subset=['age'],how='any',axis=0);
        print(ttage.isnull().sum());
        print(ttage.info());
    def p178(self):
        mage=tt['age'].mean();
        print(tt['age'].isnull().sum());
        tt['age'].fillna(mage,inplace=True);
        print(tt['age'].isnull().sum());
    def p180(self):
        et= tt['embark_town'].value_counts(dropna=True).idxmax();
        print(et);
        tt['embark_town'].fillna(et,inplace=True);
    def p181(self):
        tt['embark_town'].fillna(method='ffill',inplace=True);
    def p186(self):
        print(df3);
        mpg_to_kpl = 1.60934 / 3.78541;
        print(mpg_to_kpl);
        df3['kpl']= df3['mpg']* mpg_to_kpl;
        print(df3);
    def p188(self):
        print(df3.info());
        print(df3['hor'].unique());
        df3['hor'].replace('?',np.nan,inplace=True);
        print(df3['hor'].unique());
        df3.dropna(subset=['hor'],inplace=True);
        print(df3['hor'].unique());
        df3['hor'] =df3['hor'].astype('float');
        print(df3['hor']);
    def p190(self):
        print(df3['origin'].dtypes);
        print(df3['origin'].unique());
        df3['origin'].replace({1:'USA',2:'EU',3:'JPN'},inplace=True);
        print(df3['origin'].unique());
        print(df3['origin'].dtypes);
        df3['origin']=df3['origin'].astype('category');
        print(df3['origin'].dtypes);
    # def p192(self):
    # def p194(self):


if __name__ == '__main__':
    Part5().p194();