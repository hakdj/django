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

    def mat03(self,sy,ey):
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
        df3t['증감률'].fillna(0,inplace=True);

        df3t['year']=df3t.index;
        df3t['new_year']=pd.to_datatime(df3t.index);
        df3t['new_year']=df3t['new_year'].dt.to_period(freq='A');
        df3t.set_index(df3t['new_year'],inplace=True);

        df3t=df3t[sy:ey]
        print(df3t);

        year=df3t['new_year'].tolist;
        w=df3t['수력'].tolist();
        f=df3t['화력'].tolist();

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
        seoul_map= fol.Map(location=[37.55,126.98],zoom_start=12);
        print(TEMPLATES[0]['DIRS'])
        seoul_map.save(TEMPLATES[0]['DIRS'][0]+'/seoul_map.html')

    def mat08(self):
        seoul_map= fol.Map(location=[37.55,126.98],zoom_start=12);
        print(df4);
        df4.columns=['name','lat','lng']
        df4.set_index('name',inplace=True); #인덱스값 변경 inplace로
        for name,lat,lng in zip(df4.index,df4['lat'],df4['lng']):
            #print(name,lat,lng);
            fol.Marker([lat,lng],popup=name).add_to(seoul_map);
        seoul_map.save(TEMPLATES[0]['DIRS'][0]+'/seoul_map.html');
    def mat09(self,year):
        df5.set_index('구분',inplace=True)
        #print(df5);
        geo_path = DATA_DIRS[0]+'/data4.json';
        geo_data = json.load(open(geo_path),encoding='utf-8');
        print(geo_data);
        map=fol.Map(location=[37.5502,126.982],zoom_start=9)
        fol.Choropleth(
            geo_data=geo_data,
            data=df5[year],
            columns=[df5.index,df5[year]],
            fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.3,
            threshold_scale=[10000,100000,300000,500000,700000],
            key_on='feature.properties.name'
        ).add_to(map);
        map.save(TEMPLATES[0]['DIRS'][0]+'\\chart4result.html')
    def mat10(self):
        tt=sns.load_dataset('titanic');
        sns.set_style('whitegrid');
        fig=plt.figure(figsize=(15,5));
        ax1=fig.add_subplot(1,3,1);
        ax2=fig.add_subplot(1,3,2);
        ax3=fig.add_subplot(1,3,3);
        sns.barplot(x='sex',y='survived',data=tt,ax=ax1);
        sns.barplot(x='sex',y='survived',hue='class',data=tt,ax=ax2);
        sns.barplot(x='sex',y='survived',hue='class',dodge=False,
                    data=tt,ax=ax3);
        plt.savefig(STATICFILES_DIRS[0]+'/tt.jpg');

    def mat11(self,location):
        df2 = df.fillna(method='ffill');
        mask = (df2['전출지별'] == location) & (df2['전입지별'] != location);
        df_seoul = df2[mask];
        df_seoul = df_seoul.drop('전출지별', axis=1);
        df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True);
        df_seoul.set_index('전입지',inplace=True);
        col_years=list(map(str,range(1970,2010)));
        df_4=df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years];

        df_4=df_4.transpose();
        plt.style.use('ggplot');
        df_4.index=df_4.index.map(int);
        df_4.plot(kind='area',stacked=False,alpha=0.2,figsize=(10,5));
        plt.title('서울-> 타시도 인구 이동',size=30);
        plt.ylabel('이동 인구 수',size=20);
        plt.xlabel('기간',size=20);
        plt.legend(loc='best',fontsize=15);
        plt.savefig(STATICFILES_DIRS[0]+'/kk.jpg');

if __name__ == '__main__':
    P109().mat03();

# 장고에서 500은 서버에러





