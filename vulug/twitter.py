#!/usr/bin/python

import os
import tweepy

class Twitter(object):

    def __init__(self, config):
        self.authenticate(config)

    def get_timeline():
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
