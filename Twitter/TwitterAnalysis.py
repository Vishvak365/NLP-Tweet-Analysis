from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd 

CONSUMER_KEY = 'hhMBaP6pUxfATgBMKlTRewMfy'
CONSUMER_SECRET = 'leeCADlO8qBSAzorsU0Tg0dhmELUdQxgU8LWAF6zvVWq3qfrha'
ACCESS_TOKEN = '1374120523215540233-uWcb4zoiLmr1lEeS7H7Dq9EaE9jyOq'
ACCESS_TOKEN_SECRET = '8gZlTk8CxDvatoME2i1DqIDNMQlsVM5w4lZjAAdjAdWgQ'

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
    
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweetStream = Stream(auth, listener())
tweets = tweetStream.filter(track=['Tesla'])
