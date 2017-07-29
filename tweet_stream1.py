from nltk.twitter import Query, Streamer, Twitter, TweetViewer, credsfromfile
from nltk.corpus import twitter_samples
import csv, json
from nltk.twitter.common import json2csv
input_file = twitter_samples.abspath("tweets.20150430-223406.json")
with open(input_file) as fp:
    json2csv(fp, 'tweets.20150430-223406.tweet.csv',
            ['created_at', 'favorite_count', 'id', 'in_reply_to_status_id', 
            'in_reply_to_user_id', 'retweet_count', 'retweeted', 
            'text', 'truncated', 'user.id'])
from nltk.twitter.common import json2csv_entities
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.hashtags.csv',
                        ['id', 'text'], 'hashtags', ['text'])
    
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.user_mentions.csv',
                        ['id', 'text'], 'user_mentions', ['id', 'screen_name'])
    
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.media.csv',
                        ['id'], 'media', ['media_url', 'url'])
    
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.urls.csv',
                        ['id'], 'urls', ['url', 'expanded_url'])
    
with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.place.csv',
                        ['id', 'text'], 'place', ['name', 'country'])

with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.place_bounding_box.csv',
                        ['id', 'name'], 'place.bounding_box', ['coordinates'])

with open(input_file) as fp:
    json2csv_entities(fp, 'tweets.20150430-223406.original_tweets.csv',
                        ['id'], 'retweeted_status', ['created_at', 'favorite_count', 
                        'id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'retweet_count',
                        'text', 'truncated', 'user.id'])
