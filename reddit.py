# %%
import praw
import keras
import tensorflow as tf
import numpy as np
# %%
# Make sure the following file is in the same directory
# !WILL TAKE A FEW MINUTES TO LOAD
model = keras.models.load_model("ltsm_model_5_epoch_better.tf")
reddit = praw.Reddit(client_id='xF2jqo3z7q9uhA',
                     client_secret='jQrcUTbWclz5KO9aV1_0Ee7CPARALg',
                     user_agent='my user agent')
print(reddit.read_only)

# Type in the subreddit for the company you want to analyze
subreddit = "apple"
# Choose from one of the following timelines and change the variable -
# "hour", "week", "day", "all", "month", "year"
timeframe = "month"
# OPTIONAL - Choose the number of posts you want to analyze from segment
numPosts = 10

# %%


def analyze():
    posts = reddit.subreddit(subreddit).top(timeframe, limit=numPosts)
    comments = []
    for post in posts:
        for comment in post.comments:
            try:
                comments.append(comment.body)
            except:
                None
    preds = []
    with tf.device('CPU:0'):
        preds = model.predict(comments)
    print("The average sentiment is {} on a scale from 0 (bad) to 1(good)".format(
        np.average(preds)))


analyze()

# %%
