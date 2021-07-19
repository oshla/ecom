import tweepy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import time
import os

###My Twitter developer IDs
api_key = '2CYTvV6yHBJOq5ETxhKgKH3tj'
api_secret_key = 'lL2lBrSahmlAf5VnlvCOayqFscP6G5qeuoOqhQTeZnIKq1vlkK'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALX0QAEAAAAAYvwCZfq9POivlrVyEkxwDtNhLgs%3Dd5REQvVH3XKb8qDrULAlJQpqyaqM4r2LGhtgljDs72aSvlr9Eb'
access_token = '886578954102075392-1p8sM5SXfKRKvMDP79CCzlyWgOR60If'
access_token_secret = 'SbZF9uMAkhwtSx4xy7QoVgTswfQm1A9HUOv67GEn7fT2p'
##########################################

###Twitter authentication of IDs to grant me access to their Commands, methods and dataset
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
##########################################

# interate through list of username
df = pd.read_csv('samp_data.csv')
bata = df.columns
print(bata)
username = df['sc_handle'].tolist()
print(username)
tweetwee=[]
for i in username:
    user = i
    # Getting the Tweets of a Particular User
    # username = 'mannyconcepts'  ##Source username
    count = 10  # Amount of Tweet i want to Crawl
    ##########################################

    ###Using the Tweepy.cursor method to get the last 10 Tweets and their respective MetaData from the user
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.user_timeline, id=user).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[user, tweet.text] for tweet in tweets]
        tweetwee.extend(tweets_list)


        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
tweets_df = pd.DataFrame(tweetwee)
tweets_df = tweets_df.iloc[1: , :]
#mentdf=tweets_df.to_string(index=False)
#mentdf=pd.DataFrame(mentdf)
#print(mentdf)
tweets_df.to_csv('mentdf.csv', index=False)
##########################################