# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import json
import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
from nltk.probability import FreqDist
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

import re
from tqdm import tqdm
from sklearn.utils import shuffle
import numpy as np
import tensorflow as tf
from tqdm import tqdm
import bz2
from keras.layers import *
from keras.models import Model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
# %%
df = pd.read_pickle('amazon_review_data.pd')

# %%
df = df.sample(frac=1)

# %%
# Convert rating from double to int
df['rating'] = df['rating'].astype(int)

# %%
df['rating']

# %%
rating_1_df = df.loc[df['rating'] == 1]
rating_2_df = df.loc[df['rating'] == 2]
rating_3_df = df.loc[df['rating'] == 3]
rating_4_df = df.loc[df['rating'] == 4]
rating_5_df = df.loc[df['rating'] == 5]

# %%
rating_negative_df = rating_3_df
rating_negative_df = rating_negative_df.append(rating_2_df)
rating_negative_df = rating_negative_df.append(rating_1_df)

rating_positive_df = rating_5_df
rating_positive_df = rating_positive_df.append(rating_4_df)

rating_negative_df['rating'] = 0
rating_positive_df['rating'] = 1

# %%
numValues = min(len(rating_positive_df),len(rating_negative_df))
df.drop(df.index, inplace=True)
df = df.append(rating_positive_df[:numValues])
df = df.append(rating_negative_df[:numValues])
df = df.sample(frac=1)


# %%

# %% [markdown]
# ### USING https://www.tensorflow.org/tutorials/text/text_classification_rnn

# %%
len(df)


# %%
subset_split = 450_000
train_X,test_X,train_y,test_y = train_test_split(df['reviews'][:subset_split], df['rating'][:subset_split], test_size=0.20, random_state=42)


# %%
VOCAB_SIZE=5_000
encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens=VOCAB_SIZE)
encoder.adapt(np.array(test_X))


# %%
ltsm_model = tf.keras.Sequential([
    encoder,
    tf.keras.layers.Embedding(
        input_dim=len(encoder.get_vocabulary()),
        output_dim=64,
        # Use masking to handle the variable sequence lengths
        mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
ltsm_model.compile(loss=tf.keras.losses.mse,
              optimizer=tf.keras.optimizers.Adam(),
              metrics=['accuracy'])


# %%
with tf.device('GPU:0'):
    ltsm_model.fit(train_X, train_y, epochs=15)


# %%
# from keras.models import load_model
# ltsm_model.save('ltsm_model_15_epoch.tf')


# %%
pred = ltsm_model.predict(test_X)
pred_0_1 = []
for y in pred:
    if y > .5:
        pred_0_1.append(1)
    else:
        pred_0_1.append(0)
accuracy_score(test_y,pred_0_1)
