from nltk.twitter import Query, Streamer, Twitter, TweetViewer, credsfromfile
from nltk.twitter.common import json2csv
from nltk import sent_tokenize, word_tokenize, pos_tag
import csv

with open('tweets.20170729-064621.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    for field in row:
      tokens = word_tokenize(field)
      print tokens

