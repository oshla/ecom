import tweepy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community
#My Twitter Developer API and Token"
api_key= '2CYTvV6yHBJOq5ETxhKgKH3tj'
api_secret_key= 'lL2lBrSahmlAf5VnlvCOayqFscP6G5qeuoOqhQTeZnIKq1vlkK'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALX0QAEAAAAAYvwCZfq9POivlrVyEkxwDtNhLgs%3Dd5REQvVH3XKb8qDrULAlJQpqyaqM4r2LGhtgljDs72aSvlr9Eb'
access_token='886578954102075392-1p8sM5SXfKRKvMDP79CCzlyWgOR60If'
access_token_secret= 'SbZF9uMAkhwtSx4xy7QoVgTswfQm1A9HUOv67GEn7fT2p'
##########################################

###Twitter Authentication
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
##########################################

###Getting the ID from Twitter Username
me = api.get_user(screen_name = 'mannyconcepts')
met=me.id
print(met)
##########################################

###Extracting the User's Followers into a list
user_list = ["968425116005818368"]
follower_list = []
for user in user_list:
    followers = []
    try:
        for page in tweepy.Cursor(api.followers_ids, user_id=user).pages():
            followers.extend(page)
            print(len(followers))
    except tweepy.TweepError:
        print("error")
        continue
    follower_list.append(followers)
##########################################

###Putting the List into a Dataframe, seperating the DF into User ID and Follower's ID. User Id will be the same
df = pd.DataFrame(columns=['source','target']) #Empty DataFrame
df['target'] = follower_list[0] #Set the list of followers as the target column
df['source'] = 968425116005818368 #Set my user ID as the source
##########################################

###Creating a Network Graph of the User and the Followers
G = nx.from_pandas_edgelist(df, 'source', 'target') #Turn df into graph
pos = nx.spring_layout(G) #specify layout for visual

f, ax = plt.subplots(figsize=(10, 10))
plt.style.use('ggplot')
nodes = nx.draw_networkx_nodes(G, pos,
                               alpha=0.8)
nodes.set_edgecolor('k')
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.2)
##########################################

###Getting the Followers Usernames instead of their ID
user_list = list(df['target']) #Use the list of followers we extracted in the code above i.e. my 450 followers
for userID in user_list:
    print(userID)
    followers = []
    follower_list = []

    # fetching the user
    user = api.get_user(userID)

    # fetching the followers_count
    followers_count = user.followers_count

    try:
        for page in tweepy.Cursor(api.followers_ids, user_id=userID).pages():
            followers.extend(page)
            print(len(followers))
            if followers_count >= 5000: #Only take first 5000 followers
                break
    except tweepy.TweepError:
        print("error")
        continue
    follower_list.append(followers)
    temp = pd.DataFrame(columns=['source', 'target'])
    temp['target'] = follower_list[0]
    temp['source'] = userID
    df = df.append(temp)
    df.to_csv("networkOfFollowers.csv")
##########################################



####