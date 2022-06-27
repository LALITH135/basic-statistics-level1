# -*- coding: utf-8 -*-
"""
Created on Tue may 27 09:48:39 2022

@author: lalith kumar
"""


import pandas as pd
df = pd.read_csv('E:\\data science\\ASSIGNMENTS\\ASSIGNMENTS\\basic statistics level1\\Q7.csv')
df.shape
df.head
df.describe

# FOR POINTS

df['Points'].mean() # 3.5965625000000006
df['Points'].mode() #0    3.07
                    #1    3.92
                    #dtype: float64
                    
df['Points'].median() # 3.6950000000000003
df['Points'].var()    # 0.28588135080645166
df['Points'].describe()

'''
count    32.000000
mean      3.596563
std       0.534679
min       2.760000
25%       3.080000
50%       3.695000
75%       3.920000
max       4.930000
Name: Points, dtype: float64
'''
df['Points'].hist()

#---------------------------------------------------------------------------
# FOR SCORE

df['Score'].mean() #3.2172499999999995
df['Score'].mode() # 0    3.44
                   # dtype: float64

df['Score'].median() # 3.325
df['Score'].var()   # 0.9573789677419356
df['Score'].describe()
'''
count    32.000000
mean      3.217250
std       0.978457
min       1.513000
25%       2.581250
50%       3.325000
75%       3.610000
max       5.424000
Name: Score, dtype: float64
'''
df['Score'].hist()

#-------------------------------------------------------------------------------
# FOR WEIGH

df['Weigh'].mean() # 17.848750000000003
df['Weigh'].mode() # 0    17.02
                   # 1    18.90
                   # dtype: float64
df['Weigh'].median() #  17.71
df['Weigh'].var()    # 3.193166129032258
df['Weigh'].describe()
'''
count    32.000000
mean      3.217250
std       0.978457
min       1.513000
25%       2.581250
50%       3.325000
75%       3.610000
max       5.424000
Name: Score, dtype: float64
'''
df['Weigh'].hist()

df[['Points','Score','Weigh']].corr()

#-------------------------------------------------------------------------------








 																																					



























