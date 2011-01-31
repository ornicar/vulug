#!/usr/bin/python
import os
import curses
from vulug.twitter import Twitter
from vulug.config import Config

def render_tweet(tweet):
    print ''
    print tweet.author.screen_name
    print ''
    print tweet.text
    print '\n------------------------------'

twitter = Twitter(Config())
for tweet in twitter.get_timeline():
    render_tweet(tweet)
