#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses
from vulug.view.container import Container
from vulug.view.timeline import Timeline
from vulug.view.status import Status

class Ui(object):

    def __init__(self, term, config):
        self.term = term
        self.config = config

        height = self.term.get_height()
        width = self.term.get_width()

        self.container = Container(term, height, width)
        self.timeline = Timeline(term, height - 3, width - 4, 2, 2)
        self.status = Status(term, 1, width, height - 1, 0)

    def home(self, tweets):
        self.container.title('Home Timeline')
        self.timeline.set_tweets(tweets)
        self.unwait()

    def more(self, tweets):
        self.timeline.add_tweets(tweets)
        self.unwait()

    def wait(self):
        self.status.show('Retrieving data from twitter...')

    def unwait(self):
        self.status.show('')

    def get_key(self):
        return self.timeline.win.getch()
