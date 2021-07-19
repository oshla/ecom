import pandas as pd
from scipy.spatial.distance import pdist
import itertools
import csv
import re
import numpy as np

can=pd.read_csv('fromwebsite.csv')
can.columns=['LName','FnameAge','Sex','Age', 'TwitterU']
username=can["TwitterU"]
print(can)
can_age_normalized=(can['Age']-can['Age'].min())/(can['Age'].max()-can['Age'].min())
can_age_normalized.columns=['index','N_Age']
can_age_normalized=pd.DataFrame(can_age_normalized)
can_age_normalized=can_age_normalized.join(username)
can_age_normalized.set_index('TwitterU', inplace=True)
print(can_age_normalized)
data = can_age_normalized.values

d = pd.DataFrame(itertools.combinations(can_age_normalized.index, 2), columns=['from','to'])
d['dist'] = pdist(data, 'euclid')
print(d)
d['from2']=d['to']
d['to2']=d['from']
f=d[['from2','to2','dist']]
d= d[['from','to','dist']]
f.columns=['from','to','dist']
print(f)
print(d)
print(d.append(f,ignore_index=True))

# def Euclidean_Dist(df1, df2, cols=['x_coord','y_coord']):
#     return np.linalg.norm(df1[cols].values - df2[cols].values,
#                    axis=1)
#
# df1 = pd.DataFrame({'user_id':[214,214,214],
#                 'x_coord':[-55.2,-55.2,-55.2],
#                 'y_coord':[22.1,22.1,22.1]})
# print(df1)
#
# df2 = pd.DataFrame({'user_id':[512, 362, 989],
#                     'x_coord':[-15.2, 65.1, -84.8],
#                     'y_coord':[19.1, 71.4, 13.7]})
#
# print(df2)
# print(Euclidean_Dist(df1, df2))