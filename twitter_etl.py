import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    access_key = "tU3TSTjf0IigNMic6GVqmYpUB"
    access_secret = "esnnff49uLTve359gavwmMwvDZJYCQEhCBXRq4clw0xW8xfjS0"
    consumer_key = "1844723805362757632-eSsMXgEyFeavzOn05AZAdpLj5pF08F"
    consumer_secret = "Mn79KRK8IIWIVFtjerfBZfCNnUNDKrqZC7CNqolveRKYO"

    #Twitter Authentication

    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    #Creating an API Object
    api = tweepy.API(auth)

    #Extracting Tweets using API.user_timeline
    tweets =  api.user_timeline(screen_name = "@narendramodi", 
                                count=200,
                                include_rts = False,   # Retweets Exclude
                                tweet_mode = 'extended'  #Full text normally it only extracts 140 words
                                )


    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
                            "user" : tweet.user.screen_name,
                            "text" : text,
                            "favourite_count" : tweet.favourite_count,
                            "retweet_count" : tweet.retweet_count,
                            "created_at" :tweet.created_at
                        }

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("narendramodi_twitter_data.csv")

