## Python_Closure_Experiment.py

import pandas as pd

df = pd.read_csv('china_region.csv', usecols = ['code','region'])
df.head()

def counter(n, func, args):
    from datetime import datetime

    t1 = datetime.now()
    for i in range(n):
        func(*args)

    t2 = datetime.now()
    print("repeat {} times, cost time: {} seconds".format(n, (t2-t1).total_seconds()))

"""
接下来准备好五个版本的代码用于比较
"""

# 双参数版
def func_1(code, df):
    return df[df['code']==code]['region'].iloc[0]

# partial函数版
from functools import partial
func_2 = partial(func_1, df = df)

# lambda函数版
func_3 = lambda code:func_1(code, df)

# closure版
def outer(df):
    def inner(code):
        return df[df['code']==code]['region'].iloc[0]
    return inner
func_4 = outer(df)

# functor版
class Functor():
    def __init__(self, df):
        self.df = df
        
    def __call__(self,code):
        return df[df['code']==code]['region'].iloc[0]
func_5 = Functor(df)

# fun_6--->>>func_1
def func_6(code):
    func = lambda code:func_1(code, df)    
    return func(code)

counter(1000, func_1, [310115,df])
counter(1000, func_2, [310115])
counter(1000, func_3, [310115])
counter(1000, func_4, [310115])
counter(1000, func_5, [310115])
counter(1000, func_6, [310115])