import json
import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
# reviews = []
# rating = []
# for filename in os.listdir('data'):
#     if filename.endswith(".json"):
#         print(filename)
#         with open('data/'+filename) as f:
#             data = json.load(f)
#             for x in data:
#                 reviews.append(x['reviewText'])
#                 rating.append(x['overall'])
# data = {'reviews': reviews, 'rating': rating}
# df = pd.DataFrame(data, columns=['reviews', 'rating'])
# df.to_pickle('amazon_review_data.pd')
# df.to_csv('amazon_video.csv')
df = pd.read_pickle('amazon_review_data.pd')
# df['reviews'][0] = "asdf"
# print(df['reviews'])
tokens = []
for x in df['reviews']:
    tokens.append(word_tokenize(x))
# print(tokens)
