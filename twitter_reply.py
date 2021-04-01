# %%
import csv
import tweepy
import ssl
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
# %%
# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Microsoft'
tweet_id = '1375601268618452992'
# %%
import keras
import tensorflow as tf
model = keras.models.load_model("ltsm_model_5_epoch_better.tf")
# %%
with tf.device("CPU:0"):
    print(model.predict(["Hello there, great wheather we are having"]))
# %%
replies = []
for tweet in tweepy.Cursor(api.search, q='to:'+name, result_type='recent', timeout=999999).items(50000):
    # print(tweet)
    replies.append((tweet.created_at,tweet.text))
    # if hasattr(tweet, 'in_reply_to_status_id_str'):
        
        # if (tweet.in_reply_to_status_id_str == tweet_id):
        #     print(tweet.text)
        #     replies.append(tweet)
# with open('replies_clean.csv', 'w') as f:
#     csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
#     csv_writer.writeheader()
#     for tweet in replies:
#         row = {'user': tweet.user.screen_name,
#                'text': tweet.text.replace('\n', ' ')}
#         csv_writer.writerow(row)

# %%
text = []
import re
for reply in replies:
    temp = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",reply[1]).split())
    if len(temp) > 10:
        text.append(temp)
    # text.append(.replace('@Microsoft',''))
# %%
preds = []
with tf.device("CPU:0"):
    preds = model.predict(text)
# %%
import numpy as np
np.average(preds)
# %%
for i in range(len(text)):
    print(preds[i],text[i])
# %%
len_thing = []
for x in text:
    if len(x) < 5:
        len_thing.append(1)
print(len(len_thing))
# %%
f
# %%
print(len(f))
# %%
