#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import Config
from twitter import Twitter, TwitterAuthenticationError, TwitterMock
from view import View
from gui import Curses
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
        gui = Curses(screen, self.config)
        self.view = View(gui, self.config)
        self.home()

    def home(self):
        self.view.home(self.twitter.get_timeline())
        self.wait()

    def wait(self):
        key = self.view.get_key()
        if key == ord('j'):
            self.view.timeline.scroll(1)
        if key == ord('k'):
            self.view.timeline.scroll(-1)
        if key == ord('g'):
            self.view.timeline.scrollTop()
        if key == ord('r'):
            self.home()
        if key != ord('q'):
            self.wait()

if __name__ == "__main__":
    config = Config()
    try:
        vulug = Vulug(config)
        curses.wrapper(vulug.start)
    except VulugStopError:
        pass
