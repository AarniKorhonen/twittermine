from nltk.twitter import Query, Streamer, Twitter, TweetViewer, credsfromfile
import csv, json
from nltk.twitter.common import json2csv
from nltk.twitter.common import json2csv_entities
import pandas as pd
twitter_output = 'tweets.20170729-064621.json'
input_file = twitter_output("tweets.20170729-064621.json")
with open(input_file) as fp:
    json2csv(fp, 'tweets.20170729-064621.csv',
            ['created_at', 'favorite_count', 'id', 'in_reply_to_status_id', 
            'in_reply_to_user_id', 'retweet_count', 'retweeted', 
            'text', 'truncated', 'user.id'])

tweets = pd.read_csv('tweets.20170729-064621.csv', index_col=2, header=0, encoding="utf8")
tweets.head(5)



