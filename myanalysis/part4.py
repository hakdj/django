import matplotlib.pyplot as plt
import pandas as pd;
import seaborn as sns;
import folium as fol;
from config.settings import DATA_DIRS, STATICFILES_DIRS, TEMPLATES;

df =pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',header=0);
df2 =pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl',header=0);
df3 =pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=0);
df3.columns= ['mpg','cyl','dis','hor','wei','acc','year','origin','name'];

tt = sns.load_dataset('titanic');

class P109:
    def mat01(self):
        print(df);
        df2=df.fillna(method='ffill');
        print(df2);
        mask=(df2['전출지별']=='서울특별시') & (df2['전입지별']!='서울특별시');
        df_seoul=df2[mask];
        df_seoul=df_seoul.drop('전출지별',axis=1);
        df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True);
        df_seoul.set_index('전입지',inplace=True);
        sr_one = df_seoul.loc['경기도'];
        print(sr_one);
        plt.plot(sr_one);
        plt.title('서울 -> 경기');
        plt.savefig(STATICFILES_DIRS[0]+'/ss.jpg');
        #plt.show();

    # def mat02(self):
        # print(df);
        # df2=df.fillna(method='ffill');
        # print(df2);
        # mask=(df2['전출지별']=='서울특별시') & (df2['전입지별']!='서울특별시');
        # print(mask);
        # df_seoul=df2[mask];
        # df_seoul=df_seoul.drop('전출지별',axis=1);
        # df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True);
        # df_seoul.set_index('전입지',inplace=True);
        # sr_one = df_seoul.loc['경기도'];
        # plt.style.use('ggplot');
        # df3t.index=df3t.index.map(int)
        # df3t.plot(kind='barh',stacked=False,alpha=0.2,figsize=(10,5));
        # plt.show();

    def mat03(self):
        print(df2);
        df3=df2.loc[5:9];
        df3.drop('전력량 (억㎾h)',axis=1,inplace=True);
        print(df3);
        df3.set_index('발전 전력별',inplace=True);
        print(df3);
        df3t=df3.T;
        df3t.drop('원자력',axis=1,inplace=True);
        print(df3t);
        df3t=df3t.rename(columns={'합계':'총발전량'});
        print(df3t);
        df3t['1년전'] = df3t['총발전량'].shift(1);
        df3t['증감률'] = ((df3t['총발전량']/df3t['1년전'])-1) *100;
        print(df3t);

    def mat04(self):
        # 국가별 차량의 개수를 구하시오.
        print(df3);
        df3['count'] = 1;
        df4 = df3.groupby('origin').sum();
        df4.index = ['USA', 'EU', 'JPN']
        print(df4);
    def mat05(self):
        df4= df3[df3['origin']==1]['mpg'];
        print(df4);
    def mat06(self):
        print(tt);
        tt2=tt.pivot_table(index=['sex'],columns=['class'],aggfunc='size');
        print(tt2)

    def mat07(self):
        seoul_map= fol.Map();
        print(TEMPLATES[0]['DIRS'])
        seoul_map.save(TEMPLATES[0]['DIRS'][0]+'/seoul_map.html')


if __name__ == '__main__':
    P109().mat07();






