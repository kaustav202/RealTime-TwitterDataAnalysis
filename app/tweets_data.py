

import json

import pandas as pd

##reading the json file and importing as dataframe

tweets_json = open("tweets.json","r").read()


## split the json file with newline char , load each tweet as dictionary and store as a list of dicts

def flatten_tweets(tweets_json):
    """ Flattens out tweet dictionaries so relevant JSON
        is in a top-level dictionary."""
    tweets_list = []
    
    # Iterate through each tweet
    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)
    
        # Store the user screen name in 'user-screen_name'
        tweet_obj['user-screen_name'] = tweet_obj["user"]["screen_name"]
    
        # Check if this is a 140+ character tweet
        if 'extended_tweet' in tweet_obj:
            # Store the extended tweet text in 'extended_tweet-full_text'
            tweet_obj['extended_tweet-full_text'] = tweet_obj["extended_tweet"]["full_text"]
    
        if 'retweeted_status' in tweet_obj:
            # Store the retweet user screen name in 'retweeted_status-user-screen_name'
            tweet_obj['retweeted_status-user-screen_name'] = tweet_obj["retweeted_status"]["user"]["screen_name"]

            # Store the retweet text in 'retweeted_status-text'
            tweet_obj['retweeted_status-text'] = tweet_obj["retweeted_status"]["text"]
            if 'extended_tweet' in tweet_obj["retweeted_status"]:
                tweet_obj["retweeted_status-extended_tweet-full_text"] = tweet_obj["retweeted_status"]["extended_tweet"]["full_text"]
        if 'quoted_status' in tweet_obj:
            tweet_obj["quoted_status-text"] = tweet_obj["quoted_status"]["text"]
            if 'extended_tweet' in tweet_obj["quoted_status"]:
                tweet_obj["quoted_status-extended_tweet-full_text"] = tweet_obj["quoted_status"]["extended_tweet"]["full_text"]
        tweets_list.append(tweet_obj)
    return tweets_list

## Converts list of json into list of dictionaries




with open("tweets.json","r") as fh:
    tweets = fh.read().split("\n")

tweets = [i for i in tweets if i]
list_of_tweets  = flatten_tweets(tweets)
## storing tweets as list of dictionaries



# Create a DataFrame from `tweets`
ds_tweets = pd.DataFrame(list_of_tweets)

def get_tweets():
    return ds_tweets


