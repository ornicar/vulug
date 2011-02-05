#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import Config
from twitter import Twitter, TwitterAuthenticationError, TwitterMock
from vulug.view.ui import Ui
from term import Term
import curses

class VulugStopError(Exception):
    pass

class Vulug(object):

    mock = False

    def __init__(self, config):
        self.twitter = TwitterMock(config) if self.mock else Twitter(config)
        self.config = config
        print("Authentication with Twitter API...")
        try:
            self.twitter.authenticate_from_cache()
        except TwitterAuthenticationError:
            print("Go and bring me back the PIN: %s" % self.twitter.get_authorization_url())
            try:
                self.twitter.authenticate_from_token(raw_input('PIN:'))
                print("Success!")
            except TwitterAuthenticationError:
                print("Authentication failed. Bye.")
                raise VulugStopError

    def start(self, screen):
        term = Term(screen, self.config)
        self.ui = Ui(term, self.config)
        self.home()
        while True:
            try:
                self.handle_key()
            except KeyboardInterrupt:
                break

    def handle_key(self):
        key = self.view.get_key()
        if key == ord('j'):
            self.view.timeline.scroll(1)
            if self.view.timeline.is_scroll_near_to_end():
                self.more()
        elif key == ord('k'):
            self.view.timeline.scroll(-1)
        elif key == ord('g'):
            self.view.timeline.scroll_top()
        elif key == ord('r'):
            self.home()
        elif key == ord('q'):
            raise KeyboardInterrupt()

    def home(self):
        self.view.wait()
        self.view.home(self.twitter.get_timeline())

    def more(self):
        self.view.wait()
        self.view.more(self.twitter.more_timeline())

if __name__ == "__main__":
    config = Config()
    try:
        vulug = Vulug(config)
        curses.wrapper(vulug.start)
    except VulugStopError:
        pass
