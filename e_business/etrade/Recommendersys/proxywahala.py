import pandas as pd
import csv
df= pd.read_csv('bosuntweets101.csv')
df=pd.DataFrame(data=df['1'])
print(df.to_string(index=False))