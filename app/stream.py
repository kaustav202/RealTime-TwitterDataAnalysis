
import tweepy
from tweepy import Stream
import twitter_config as tc

# authorize the API Key
authentication = tweepy.OAuthHandler(tc.api_key, tc.api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(tc.access_token, tc.access_token_secret)

# call the api
api = tweepy.API(authentication)

#tweepy.models.Status




from tweepy.streaming import StreamListener
import json
import time
import sys

class SListener(StreamListener):
    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open(self.fprefix , 'w')


    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)
            if (self.counter % 50 == 0):
                print("No of tweets currently in tweets.json = ", self.counter)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print("WARNING: %s" % warning['message'])
            return


    def on_status(self, status):
        self.output.write(status)
        self.counter += 1
        # if (self.counter % 50 == 0):
        #     print("No of tweets currently in tweets.json = ", self.counter)
        if self.counter >= 20000:
            self.output.close()
            self.output  = open( self.fprefix , 'w')
            self.counter = 0
        return


    def on_delete(self, status_id, user_id):
        print("Delete notice")
        return


    def on_limit(self, track):
        print("WARNING: Limitation notice received, tweets missed: %d" % track)
        return


    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return 


    def on_timeout(self):
        print("Timeout, sleeping for 60 seconds...")
        time.sleep(60)
        return 



# Set up words to track
keywords_to_track = ['#google', '#apple']

# Instantiate the SListener object 

file_to_write = "tweets.json"

listen = SListener(api , file_to_write)

# Instantiate the Stream object
stream = Stream(authentication, listen)

# Begin collecting data
stream.filter(track = keywords_to_track)

