

import numpy as np
import matplotlib.pyplot as plt
from tweets_data import get_tweets
from sentiment_analysis import sentiment
import pandas as pd













sentiment.set_hashtag_data('5T','#apple','#google') #interval first then hashtags




ds_tweets = get_tweets()

python = sentiment.get_hashtag_data()['#google']

# Find mentions of #rstats in all text fields
rstats = sentiment.get_hashtag_data()['#apple']
# Print proportion of tweets mentioning #python
print("Proportion of #google tweets:", np.sum(python) / ds_tweets.shape[0])

# Print proportion of tweets mentioning #rstats
print("Proportion of #apple tweets:", np.sum(rstats) / ds_tweets.shape[0])




ds_tweets['created_at'] = pd.to_datetime(ds_tweets["created_at"])

ds_tweets = ds_tweets.set_index("created_at")



ds_tweets['google'] = sentiment.get_hashtag_data()['#google']

ds_tweets['apple'] = sentiment.get_hashtag_data()['#apple']

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
sentiment.graph()
