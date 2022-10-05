

import numpy as np
import matplotlib.pyplot as plt
from tweets_data import get_tweets
import sentiment_analysis
import pandas as pd




ds_tweets = get_tweets()




sentiments  = sentiment_analysis.SentimentalAnalysis(ds_tweets=ds_tweets)
sentiments.set_hashtag_data('5T','#apple','#google')
sentiments.graph()





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
    return contains_column

## This function checks columns for presence of keywords(boolean list)


ds_tweets = get_tweets()

python = check_word_in_tweet('#google', ds_tweets)

# Find mentions of #rstats in all text fields
rstats = check_word_in_tweet('#apple', ds_tweets)

# Print proportion of tweets mentioning #python
print("Proportion of #google tweets:", np.sum(python) / ds_tweets.shape[0])

# Print proportion of tweets mentioning #rstats
print("Proportion of #apple tweets:", np.sum(rstats) / ds_tweets.shape[0])




ds_tweets['created_at'] = pd.to_datetime(ds_tweets["created_at"])

ds_tweets = ds_tweets.set_index("created_at")



ds_tweets['google'] = check_word_in_tweet('#google', ds_tweets)

ds_tweets['apple'] = check_word_in_tweet('#apple', ds_tweets)

sum_google = ds_tweets['google'].resample('5T').sum()

sum_apple = ds_tweets['apple'].resample('5T').sum()

plt.plot(sum_google , color = 'blue')
plt.plot(sum_apple , color = 'red')

plt.xlabel('minute'); plt.ylabel('Tweet Count')
plt.title('Total mentions over time')
plt.legend(('#google', '#apple'))
plt.show()




mean_google = ds_tweets['google'].resample('5T').mean()

mean_apple = ds_tweets['apple'].resample('5T').mean()

plt.plot(mean_google , color = 'blue')
plt.plot(mean_apple , color = 'red')

plt.xlabel('minute'); plt.ylabel('Percentage')
plt.title('Average mentions over time')
plt.legend(('#google', '#apple'))
plt.show()
