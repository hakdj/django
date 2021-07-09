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
df4 = pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl');
df5 = pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl');

stock = pd.read_excel(DATA_DIRS[0]+'//stock.xlsx',engine='openpyxl');
#주가데이터
stock = pd.read_excel(DATA_DIRS[0]+'//stock price.xlsx',engine='openpyxl');
#주식가격
stock = pd.read_excel(DATA_DIRS[0]+'//stock valuation.xlsx',engine='openpyxl');
#주식정보


tt = sns.load_dataset('titanic');
# titanic

class Util:
    def add10(self,n):
        return n+10;
    def add_two(self,a,b):
        return a+b;
    def min_max(self,x):
        return x.max() -x.min();
    def kpl(self,mpg,cyl):
        return mpg * (1.6/3.7)+cyl;
    def m_value(self,x):
        return x.isnull();
    def m_count(self,x):
        return self.m_value(x).sum();
    def total(self,df):
        return self.m_count(df).sum();
    def display(self,df):
        return df.info();

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
    def p221(self):
        #tt.apply(Util().add10);
        df=tt.loc[:,['age','fare']];
        print(df);
        df2=df.apply(Util().add10,axis=0);
        print(df2);
        df3=df.apply(Util().min_max,axis=1);
        print(df3);
        df4=df.apply(Util().min_max,axis=0);
        print(df4);
        df5=df.apply(lambda x:Util().add_two(x['age'],x['fare']), axis=1);
        print(df5);
    def p221test(self):
        print(df3);
        # df3 df에 kpl이라는 컬럼에 kpl 정보를 입력 하시오.
        df3['kpl']=df3.apply(lambda x:Util().kpl(x['mpg'],x['cyl']),axis=1);
        print(df3);
    def p226(self):
        result=tt.pipe(Util().display); # pipe를 이용하여 데이타 프레임을 넣어준다.
        print(result);
        result2=tt.loc[:,['age','fare']].pipe(Util().total);
        print(result2);
    def p229(self):
        df=tt.loc[0:4,'survived':'age'];
        print(df);
        columns=df.columns.values;
        sort_column= sorted(columns);
        df_sort = df[sort_column];
        print(df_sort);

        new_df=df[['sex','age','survived','pclass']];
        print(new_df)
    def p232(self):
        print(stock.info());
        print(stock);
        stock['연월일']=stock['연월일'].astype('str');
        datas=stock['연월일'].str.split('-');
        print(datas);
        stock['연']=datas.str.get[0];
        stock['월']=datas.str.get[1];
        stock['일']=datas.str.get[2];
        print(stock);
    def p234(self):
        mask = (tt['age']>=10) & (tt['age']<20);
        mask2 = (tt['age']>=10) & (tt['sex']=='female');
        mask3 = (tt['age']<10) | (tt['age'] > 60);
        tt2=tt.loc[mask3,['age','sex','pclass']];
        print(tt2);
        pd.set_option('display.max_columns',10);
        mask10 = tt['pclass']==1;
        mask20 = tt['pclass']==2;
        mask30 = tt['pclass']==3;
        tt3=tt[mask20|mask30];
        print(tt3);
        tt4=tt['pclass'].isin([2,3]);
        print(tt4);



if __name__ == '__main__':
    Part6().p234();