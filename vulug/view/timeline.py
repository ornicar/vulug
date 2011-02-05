#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses
import textwrap
from vulug.view import Helper

class Timeline(object):

    def __init__(self, gui, height, width, y, x):
        self.height, self.width, self.y, self.x = height, width, y, x
        self.gui = gui
        self.scroll_value = 0
        self.lines = []
        self.nb_lines = 1
        self.init()

    def set_tweets(self, tweets):
        self.lines = []
        self.add_tweets(tweets)

    def add_tweets(self, tweets):
        for tweet in tweets:
            textlines = textwrap.wrap(self.gui.text(tweet.text), 60)
            self.lines.append([self.gui.text(tweet.author.screen_name), self.gui.get_user_color()])
            for textline in textlines:
                self.lines.append([textline, None])
            self.lines.append([pretty_date(tweet.created_at), self.gui.get_discret_color()])
            self.lines.append(['', None])
            self.lines.append(['', None])
        self.resize()
        for line in self.lines:
            self.win.addstr(line[0] + '\n', line[1] or self.gui.get_standard_color())
        self.refresh()

    def scroll(self, lines):
        self.scroll_value += lines
        self.scroll_value = min(self.scroll_value, self.scroll_max)
        self.scroll_value = max(self.scroll_value, 0)
        self.refresh()

    def scroll_top(self):
        self.scroll_value = 0
        self.refresh()

    def is_scroll_near_to_end(self):
        return 10 > (self.scroll_max - self.scroll_value)

    def resize(self):
        self.nb_lines = max(len(self.lines) + 1, self.height)
        self.scroll_max = self.nb_lines - self.height - 1
        del self.win
        self.init()

    def init(self):
        self.win = curses.newpad(self.nb_lines, self.width)
        self.win.bkgd(self.gui.get_standard_color())

    def refresh(self):
        self.win.refresh(self.scroll_value, 0, self.y, self.x, self.height, self.width)

