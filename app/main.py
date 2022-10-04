
import numpy as np
import matplotlib.pyplot as plt
from tweets_data import get_tweets
import sentiment_analysis
import pandas as pd




ds_tweets = get_tweets()


sentiments  = sentiment_analysis.SentimentalAnalysis(ds_tweets=ds_tweets)
sentiments.set_hashtag_data('5T','#apple','#google')
sentiments.graph()
