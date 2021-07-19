import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain
cov= pd.read_csv('bosuntweets')
new_df = cov['source'].str.split(',',expand=True)
new_df.columns=['source1', 'destination']
new_df['destination'] = new_df['destination'].str.replace('\n', '')


G = nx.from_pandas_edgelist(new_df,'source1', 'destination', create_using=nx.DiGraph())
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
# G_sorted = pd.DataFrame(sorted(G.degree, key=lambda x: x[1], reverse=True))
# G_sorted.columns = ['nconst','degree']
# print(G_sorted.head())
#
# G_tmp = nx.k_core(G, 1) #Exclude nodes with degree less than 10
#
# partition = community_louvain.best_partition(G_tmp)
# #Turn partition into dataframe
# partition1 = pd.DataFrame([partition]).T
# partition1 = partition1.reset_index()
# partition1.columns = ['names','group']
# print(partition1.head())
#
# G_sorted = pd.DataFrame(sorted(G_tmp.degree, key=lambda x: x[1], reverse=True))
# G_sorted.columns = ['names','degree']
# print(G_sorted.head())
# dc = G_sorted
#
# combined = pd.merge(dc,partition1, how='left', left_on="names",right_on="names")
#
# pos = nx.spring_layout(G_tmp)
# f, ax = plt.subplots(figsize=(10, 10))
# plt.style.use('ggplot')
# #cc = nx.betweenness_centrality(G2)
# nodes = nx.draw_networkx_nodes(G_tmp, pos,
#                                cmap=plt.cm.Set1,
#                                node_color=combined['group'],
#                                alpha=0.8)
# nodes.set_edgecolor('k')
# nx.draw_networkx_labels(G_tmp, pos, font_size=8)
# nx.draw_networkx_edges(G_tmp, pos, width=1.0, alpha=0.2)
# h= G_tmp.to_directed()
# print(list(h.edges))
# nx.draw(h)
# plt.show()
# plt.savefig('twitterFollowers2.png')
#
#
# print(new_df)

#df['Grade'] = df['Grade'].str.replace('%', '')
cov= pd.read_csv('bigtweets')
a= [['wazobia,stop'],['wazobia, stop'],['wazo, stop']]
result= dict((i,a.count(i)) for i in a)
print(result)

