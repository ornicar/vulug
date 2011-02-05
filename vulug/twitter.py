#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import random
from datetime import datetime

class TwitterAuthenticationError(Exception):
    pass

class Twitter(object):

    def __init__(self, config):
        self.config = config
        self.auth = tweepy.OAuthHandler(self.config.consumer_token, self.config.consumer_secret)
        self.page = 1

    def get_timeline(self):
        self.page = 1
        return self.api.home_timeline(page=self.page)

    def more_timeline(self):
        self.page += 1
        return self.api.home_timeline(page=self.page)

    def authenticate_from_cache(self):
        try:
            with open(self.config.token_file, 'r') as token_resource:
                token = token_resource.readlines()
                self.auth.set_access_token(token[0].rstrip('\n'), token[1])
                self.api = tweepy.API(self.auth)
        except (IOError, tweepy.TweepError):
            raise TwitterAuthenticationError

    def authenticate_from_token(self, token):
        try:
            self.auth.get_access_token(token)
            token_string = self.auth.access_token.key + '\n' + self.auth.access_token.secret
            with open(self.config.token_file, 'w') as token_resource:
                token_resource.write(token_string)
            self.api = tweepy.API(self.auth)
        except (IOError, tweepy.TweepError):
            raise TwitterAuthenticationError

    def get_authorization_url(self):
        return self.auth.get_authorization_url()

class TwitterMock(object):

    def __init__(self, config):
        pass;

    def authenticate_from_cache(self):
        return True

    def get_timeline(self):
        results = list()
        usernames = ['cat', 'window', 'defenestrate', 'AuDiableVauvert', 'github']
        texts = ["This account references all Linux users. Just follow @iuselinux to get listed.", "KDE SC 4.6 to [extra]: Andrea Scarpino wrote: KDE announced the availability of its Software Compilation 4.6. Yo... http://bit.ly/fv2g76", '"You autocomplete me."', u"@n1k0 Huhu ! J'avais oublié cette appli ! ;) Bien ouej"]
        for it in xrange(30):
            json = {
                'user': {'screen_name': random.choice(usernames)},
                'text': random.choice(texts),
                'created_at': "Wed May 26 20:35:12 +0000 2010"
            }
            results.append(tweepy.Status.parse(None, json))
        return results
