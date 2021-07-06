import pandas as pd;

class P001:
    def series01(self):
        list_data=['202007',3.14,'ABC',100,True]
        sr =pd.Series(list_data);
        print(sr);
        sr2=sr.tolist();
        print(sr2);
        print(sr.index);
        print(sr.values);
        print(sr[1]);
        print(sr[1:3]);


    # def data02(self)
    #
    #     print(df):
    #     df.set)index('이름'inplace=True)
    #     d1=df.loc['영희','수학':'과학'];
    #     print(d1);

    #
    # def df05(self):
    #     print(df);
    #     df.loc['D']=[99,88,77,66];
    #     print(df);



if __name__ == '__main__':
    P001().series01();