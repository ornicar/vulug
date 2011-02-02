#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses

screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
screen.clear()
screen.attrset(0)
screen.addstr('Hello')
screen.attrset(curses.A_BOLD)
screen.addstr('Hello')
screen.attrset(curses.color_pair(1))
screen.addstr('Hello')
screen.refresh()
curses.napms(1000)
curses.endwin()
