

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweets_data import get_tweets
import pandas as pd
import matplotlib as plt



class SentimentalAnalysis:
    def __init__(self,ds_tweets = get_tweets()):
        # Instantiate new SentimentIntensityAnalyzer
        self.sid = SentimentIntensityAnalyzer()
        #Date fixes the error so the index will be a date rather than the normal index
        self.dates = pd.to_datetime(ds_tweets['created_at'])
        self.ds_tweets = ds_tweets.set_index(self.dates)

        #set it to apple for now
        self.hashtag = '#apple' 
        #set it to 5 minutes for now
        self.interval = '5T'
        # We need to add dates for both adding it to the graph and for the sentiment analysis to be able to record the time
        
        self.sentiment_scores = self.ds_tweets['text'].apply(self.sid.polarity_scores)
        
        self.sentiment = self.sentiment_scores.apply(lambda x: x["compound"])
        self.interval = '5T'

    #Helper for sentiment
    def check_word_in_tweet(self,word, data):
    
        ## ill be treating this as a helper function for get_sentiment
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
        print(type(contains_column))
        return contains_column

    #for us to set the sentiment
    def set_sentiment(self,hashtag='#apple', interval='5T'):
        self.hashtag = hashtag
        self.interval = interval
        self.sentiment = self.sentiment[self.check_word_in_tweet(self.hashtag,self.ds_tweets)].resample(interval).mean()
        return None
    


    #another helper function to help us generate the graph and will get us the scores 
    def get_sentiment(self,hashtag ='#apple',interval = '5T'):
        #generate sentiment scores
        return self.sentiment
    
    #gets graph
    def graph(self):
        plt.plot(self.get_sentiment(),color='blue')

        plt.xlabel('seconds')
        plt.ylabel('Sentiment')
        plt.title('Sentiment of Tweets');
        plt.legend((self.hashtag))
        plt.show()
   

        
    












'''







def check_word_in_tweet(word, data):
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
    print(type(contains_column))
    return contains_column










# Instantiate new SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

ds_tweets = get_tweets()

dates = pd.to_datetime(ds_tweets['created_at'])
ds_tweets = get_tweets().set_index(dates)


# Generate sentiment scores
sentiment_scores = ds_tweets['text'].apply(sid.polarity_scores)


sentiment = sentiment_scores.apply( lambda x: x["compound"] )


# Print out the text of a negative twee

# Generate average sentiment scores for #python
sentiment_go = sentiment[ check_word_in_tweet('#google', ds_tweets) ].resample('10S').mean()

# Generate average sentiment scores for #rstats
sentiment_ap = sentiment[ check_word_in_tweet('#apple', ds_tweets) ].resample('10S').mean()


# generate one more with a popular hashtag #fashion
sentiment_fa = sentiment[check_word_in_tweet('#fashion',ds_tweets)].resample('10S')

#print(sentiment_go)
# Import matplotlib
import matplotlib.pyplot as plt

# Plot average #python sentiment per day
#plt.plot(sentiment_go, color = 'blue')

# Plot average #rstats sentiment per day
#plt.plot(sentiment_ap, color = 'red')

#plt.xlabel('seconds')
#plt.ylabel('Sentiment')
#plt.title('Sentiment of Tweets ')
#plt.legend(('#google', '#apple'))
#plt.show()


        
        
        
'''


