#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses

class View(object):

    def __init__(self, gui, config):
        self.gui = gui
        self.config = config

        height = self.gui.get_height()
        width = 80 # it's large enough
        width = self.gui.get_width()

        self.container = Container(gui, height, width)
        self.timeline = Timeline(gui, height - 3, width - 4, 2, 2)
        self.status = Status(gui, 1, width, height - 1, 0)

    def home(self, tweets):
        self.container.title('Home Timeline')
        self.status.show('Fetching home timeline...')
        self.timeline.render_tweets(tweets)
        self.status.show('Done.')

    def ask(self, question):
        win = curses.newwin(5, self.width, 2, 2)
        self.configure(win)
        win.addstr(question)
        win.refresh()
        input = win.getstr()
        return input

    def get_key(self):
        return self.timeline.win.getch()

class Timeline(object):

    def __init__(self, gui, height, width, y, x):
        win = curses.newpad(3000, width)
        win.bkgd(gui.get_standard_color())
        self.height, self.width, self.y, self.x = height, width, y, x
        self.gui, self.win = gui, win
        self.scrollValue = 0
        self.refresh()

    def render_tweets(self, tweets):
        self.win.clear()
        for tweet in tweets:
            self.win.addstr(self.gui.text(tweet.author.screen_name) + '\n', self.gui.get_user_color())
            self.win.addstr(self.gui.text(tweet.text) + '\n\n\n', self.gui.get_standard_color())
        self.refresh()

    def scroll(self, lines):
        self.scrollValue += lines
        if self.scrollValue < 0:
            self.scrollValue = 0
        else:
            self.refresh()

    def scrollTop(self):
        self.scrollValue = 0
        self.refresh()

    def refresh(self):
        self.win.refresh(self.scrollValue, 0, self.y, self.x, self.height, self.width)

class Status(object):

    def __init__(self, gui, height, width, y, x):
        win = curses.newwin(height, width, y, x)
        win.bkgd(gui.get_standard_color())
        self.gui, self.win = gui, win

    def show(self, text):
        self.win.clear()
        self.win.addstr(self.gui.text(text), self.gui.get_discret_color())
        self.win.refresh()

class Container(object):

    def __init__(self, gui, height, width):
        win = curses.newwin(height, width, 0, 0)
        win.bkgd(gui.get_standard_color())
        bar = "_" * width
        win.addstr(0, 0, bar, curses.color_pair(3))
        win.addstr(height - 2, 0, bar, curses.color_pair(3))
        win.refresh()
        self.height, self.width = height, width
        self.gui, self.win = gui, win

    def title(self, title):
        position = (self.width + 4 - len(title))/2
        self.win.addstr(0, int(position), '%s' % self.gui.text(title), self.gui.get_discret_color())
        self.win.refresh()
