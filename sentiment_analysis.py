
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Instantiate new SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Generate sentiment scores
sentiment_scores = ds_tweets['text'].apply(sid.polarity_scores)


sentiment = sentiment_scores.apply( lambda x: x["compound"] )


# Print out the text of a negative twee

# Generate average sentiment scores for #python
sentiment_go = sentiment[ check_word_in_tweet('#google', ds_tweets) ].resample('5T').mean()

# Generate average sentiment scores for #rstats
sentiment_ap = sentiment[ check_word_in_tweet('#apple', ds_tweets) ].resample('5T').mean()


# Import matplotlib
import matplotlib.pyplot as plt

# Plot average #python sentiment per day
plt.plot(sentiment_go, color = 'blue')

# Plot average #rstats sentiment per day
plt.plot(sentiment_ap, color = 'red')

plt.xlabel('minute')
plt.ylabel('Sentiment')
plt.title('Sentiment of Tweets ')
plt.legend(('#google', '#apple'))
plt.show()
