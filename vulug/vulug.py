#!/usr/bin/python
import os
import curses
import tweepy

class Config(object):

    def __init__(self):
        self.token_file = os.getenv('HOME') + '/.vulugtoken'
        self.consumer_token = "EhwAZOq7z4FYGMK0aiDNg"
        self.consumer_secret = "1RiNS0idivgDO8YOW6lLRR72QQkDfOAaqVjtjaPmI"

class Twitter(object):

    def __init__(self, config):
        self.authenticate(config)

    def get_timeline(self):
        return self.api.home_timeline()

    def authenticate(self, config):
        print "Trying to authenticate to twitter API..."
        auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
        try:
            with open(config.token_file, 'r') as token_resource:
                token = token_resource.readlines()
                auth.set_access_token(token[0].rstrip('\n'), token[1])
        except (IOError, tweepy.TweepError):
            print("Go and bring me back the PIN: %s" % auth.get_authorization_url())
            auth.get_access_token(raw_input('PIN:'))
            token_string = auth.access_token.key + '\n' + auth.access_token.secret
            with open(config.token_file, 'w') as token_resource:
                token_resource.write(token_string)
        self.api = tweepy.API(auth)

class Renderer(object):

    def render_tweet(self, tweet):
        print '\n' + tweet.author.screen_name
        print '\n' + tweet.text
        print '\n' + '------------------------------'

twitter = Twitter(Config())
renderer = Renderer()

for tweet in twitter.get_timeline():
    renderer.render_tweet(tweet)
