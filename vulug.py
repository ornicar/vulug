#!/usr/bin/python
import os
import curses
import tweepy

def render_tweet(tweet):
    print ''
    print tweet.author.screen_name
    print ''
    print tweet.text
    print '\n------------------------------'

token_file = os.getenv('HOME') + '/.vulugtoken'
consumer_token = "EhwAZOq7z4FYGMK0aiDNg"
consumer_secret = "1RiNS0idivgDO8YOW6lLRR72QQkDfOAaqVjtjaPmI"
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

print "Trying to authenticate to twitter API..."
try:
    with open(token_file, 'r') as token_resource:
        token = token_resource.readlines()
        auth.set_access_token(token[0].rstrip('\n'), token[1])
except (IOError, tweepy.TweepError):
    print("Go and bring me back the PIN: %s" % auth.get_authorization_url())
    auth.get_access_token(raw_input('PIN:'))
    token_string = auth.access_token.key + '\n' + auth.access_token.secret
    with open(token_file, 'w') as token_resource:
        token_resource.write(token_string)

api = tweepy.API(auth)
tweets = api.home_timeline()
for tweet in tweets:
    render_tweet(tweet)
