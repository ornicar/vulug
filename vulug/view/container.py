#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses

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
