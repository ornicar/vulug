#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import locale

class Config(object):

    def __init__(self):
        self.token_file = os.getenv('HOME') + '/.vulugtoken'
        self.consumer_token = "EhwAZOq7z4FYGMK0aiDNg"
        self.consumer_secret = "1RiNS0idivgDO8YOW6lLRR72QQkDfOAaqVjtjaPmI"
        self.screen_delay = .1 # Seconds between screen updates.
        locale.setlocale(locale.LC_ALL, '')
        self.code = locale.getpreferredencoding()
