import matplotlib.pyplot as plt
import pandas as pd;
import numpy as np;

from config.settings import DATA_DIRS


class P108:
    def p108(self):
        df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',
                           engine='openpyxl',header=0);
        # 데이타 폴더 안에있는 값 가져오기
        #print(df);
        df=df.fillna(method='ffill');
        #누락값(NaN)을 앞 데이터로 채움(엑셀 양식 병합 부분)
        mask=(df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시');
        df_seoul=df[mask];
        df_seoul=df_seoul.drop('전출지별',axis=1);
        df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True);
        # inplace는 데이터를 이름을 바꾸지않고 그자체에서 바꾸게 해주는 옵션임
        df_seoul.set_index('전입지',inplace=True);
        #어떠한 특정 컬럼을 index 시킨다.
        sr_one = df_seoul.loc['경기도'];
        # 분석데이터를 리스트안에 딕셔너리로 만들기(하이차트를 쓰기위해)
        result=[];
        d={};
        d['name']='경기도';
        d['data']=sr_one.values.tolist();
        result.append(d);
        #print(result);
        return result;
        #데이터를 만들어내서 리턴해주는게 이 함수의 역할임.


        #print(sr_one);
        #print(sr_one.head());
        # head 나 tail을 이용해서 데이터의 앞과 뒤를 통해서 내가 얻는 데이터의
        # 형태등을 파악할수 있다.
        plt.plot(sr_one.index,sr_one.values);
        plt.show();



if __name__ == '__main__':
    P108().p108();