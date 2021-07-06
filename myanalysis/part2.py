import pandas as pd;
import numpy as np;

from config.settings import DATA_DIRS

data={
    '국어':[93,83,90],
    '영어':[93,83,90],
    '수학':[93,83,90],
    '과학':[92,82,72]
};

df=pd.DataFrame(data,index=['A','B','C'])

class P058:
    def r1(self):
        df.to_csv(DATA_DIRS[0]+'//testdata.csv');
        df.to_json(DATA_DIRS[0]+'//testdata.json');
        df.to_excel(DATA_DIRS[0]+'//testdata.xlsx');

if __name__ == '__main__':
     P058().r1();
