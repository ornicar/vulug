#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses

class Term(object):

    def __init__(self, screen, config):
        curses.use_default_colors()
        curses.curs_set(0)
        self.colors = [
            [ curses.COLOR_WHITE, 233 ],
            [ 29, 233 ],
            [ 242, 233 ]
        ]
        for i, pair in enumerate(self.colors):
            curses.init_pair(i+1, pair[0], pair[1])
        screen.bkgd(self.get_standard_color())
        self.screen, self.config = screen, config

    def get_height(self):
        height, width = self.screen.getmaxyx()
        return height

    def get_width(self):
        height, width = self.screen.getmaxyx()
        return width

    def get_standard_color(self):
        return self.get_color(1)

    def get_user_color(self):
        return self.get_color(2)

    def get_discret_color(self):
        return self.get_color(3)

    def get_color(self, code):
        return curses.color_pair(code)

    def text(self, string):
        return string.encode(self.config.code)
