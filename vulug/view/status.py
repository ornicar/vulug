#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses

class Status(object):

    def __init__(self, gui, height, width, y, x):
        win = curses.newwin(height, width, y, x)
        win.bkgd(gui.get_standard_color())
        self.gui, self.win = gui, win

    def show(self, text):
        self.win.clear()
        self.win.addstr(self.gui.text(text), self.gui.get_discret_color())
        self.win.refresh()

