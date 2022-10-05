from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweets_data import get_tweets
import pandas as pd
import matplotlib.pyplot as plt

class SentimentalAnalysis:
    def __init__(self,ds_tweets = get_tweets()):
        self.sid = SentimentIntensityAnalyzer()
        self.dates = pd.to_datetime(ds_tweets['created_at'])
        self.ds_tweets = ds_tweets.set_index(self.dates)
        self.hashtag = {}
        self.interval = '5T'
        self.sentiment_scores = self.ds_tweets['text'].apply(self.sid.polarity_scores)
        self.sentiment = self.sentiment_scores.apply(lambda x: x["compound"])

    def check_word_in_tweet(self,word, data):## This function checks columns for presence of keywords(boolean list)
       
        """Checks if a word is in a Twitter dataset's text. 
        Checks text and extended tweet (140+ character tweets) for tweets,
        retweets and quoted tweets.
        Returns a logical pandas Series.
        """
        contains_column = data['text'].str.contains(word, case = False)
        contains_column |= data['extended_tweet-full_text'].str.contains(word, case = False)
        contains_column |= data["quoted_status-text"].str.contains(word, case = False)
        contains_column |= data["quoted_status-extended_tweet-full_text"].str.contains(word, case = False)
        contains_column |= data["retweeted_status-text"].str.contains(word, case = False)
        contains_column |= data["retweeted_status-extended_tweet-full_text"].str.contains(word, case = False)
       
        return contains_column

 
    def set_hashtag_data(self, interval='5T',*argv):
        for hashtags in argv:
            self.hashtag[hashtags] = self.sentiment[self.check_word_in_tweet(hashtags,self.ds_tweets)].resample(interval).mean()
        self.interval = interval
        return None
    
    def get_hashtag_data(self):
        return self.hashtag
    
    def graph(self):
    
        if(len(self.hashtag) == 0):
            return False 

        for keys in self.hashtag:
            plt.plot(self.hashtag[keys])
        plt.xlabel('minutes')
        plt.ylabel('Sentiment')
        plt.title('Sentiment of Tweets');
        plt.legend(self.hashtag.keys())
        plt.show()



sentiment = SentimentalAnalysis(ds_tweets=get_tweets())
