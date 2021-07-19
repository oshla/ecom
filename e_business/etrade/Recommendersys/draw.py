import tweepy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain

api_key= '2CYTvV6yHBJOq5ETxhKgKH3tj'
api_secret_key= 'lL2lBrSahmlAf5VnlvCOayqFscP6G5qeuoOqhQTeZnIKq1vlkK'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALX0QAEAAAAAYvwCZfq9POivlrVyEkxwDtNhLgs%3Dd5REQvVH3XKb8qDrULAlJQpqyaqM4r2LGhtgljDs72aSvlr9Eb'
access_token='886578954102075392-1p8sM5SXfKRKvMDP79CCzlyWgOR60If'
access_token_secret= 'SbZF9uMAkhwtSx4xy7QoVgTswfQm1A9HUOv67GEn7fT2p'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

df = pd.read_csv("networkOfFollowers.csv") # Read into a df
print(df)
G = nx.from_pandas_edgelist(df,'source', 'target')

G_sorted = pd.DataFrame(sorted(G.degree, key=lambda x: x[1], reverse=True))
G_sorted.columns = ['nconst','degree']
print(G_sorted.head())

G_tmp = nx.k_core(G, 1) #Exclude nodes with degree less than 10

partition = community_louvain.best_partition(G_tmp)
#Turn partition into dataframe
partition1 = pd.DataFrame([partition]).T
partition1 = partition1.reset_index()
partition1.columns = ['names','group']
print(partition1.head())

G_sorted = pd.DataFrame(sorted(G_tmp.degree, key=lambda x: x[1], reverse=True))
G_sorted.columns = ['names','degree']
print(G_sorted.head())
dc = G_sorted

combined = pd.merge(dc,partition1, how='left', left_on="names",right_on="names")
pos = nx.spring_layout(G_tmp)
f, ax = plt.subplots(figsize=(10, 10))
plt.style.use('ggplot')
#cc = nx.betweenness_centrality(G2)
nodes = nx.draw_networkx_nodes(G_tmp, pos,
                               cmap=plt.cm.Set1,
                               node_color=combined['group'],
                               alpha=0.8)
nodes.set_edgecolor('k')
nx.draw_networkx_labels(G_tmp, pos, font_size=8)
nx.draw_networkx_edges(G_tmp, pos, width=1.0, alpha=0.2)
plt.savefig('twitterFollowers.png')


