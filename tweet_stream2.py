from nltk.twitter import Query, Streamer, Twitter, TweetViewer, credsfromfile
oauth = credsfromfile()
client = Query(**oauth)
tw = Twitter()
tw.tweets(keywords='white privilege, #blacklivesmatter', to_screen=False, limit=25)

