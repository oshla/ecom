import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

cov= pd.read_csv('bigtweets')
new_df = cov['source'].str.replace(',','-')
print(new_df)
new_df=new_df.str.replace('\n','')
new_df.columns=['source']

new_df= pd.DataFrame(new_df)
print(new_df)
print(new_df['source'].value_counts())