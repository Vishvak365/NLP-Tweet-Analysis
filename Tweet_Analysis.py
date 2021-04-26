import tensorflow as tf
import keras
import csv
import tweepy
import numpy as np
import ssl
import re
import twitter_secrets
ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = twitter_secrets.consumer_key
consumer_secret = twitter_secrets.consumer_secret
access_token = twitter_secrets.access_token
access_token_secret = twitter_secrets.access_token_secret

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# model being loaded
model = keras.models.load_model("ltsm_model_5_epoch_better.tf")

def tweet_analyzer(name: str, tweet_id: str):
    replies = []
    text = []
    for tweet in tweepy.Cursor(api.search, q='to:'+name, result_type='recent', timeout=999999).items(50):
        replies.append((tweet.created_at,tweet.text))
    for reply in replies:
        temp = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",reply[1]).split())
        if len(temp) > 10:
            text.append(temp)
    preds = []
    with tf.device("CPU:0"):
        preds = model.predict(text)
    average_sentiment_score = np.average(preds)

    score_reply = []
    for i in range(len(text)):
        print('Score', 'Replies')
        print(preds[i],text[i])
        score_reply.append((preds[i],text[i]))
    print('Average Score: {}'.format(average_sentiment_score))

    return average_sentiment_score, score_reply
    

    
