#!/usr/bin/python

import dbus
import sys

import player

try:
    mp,props = player.getPlayer()
except:
    sys.exit(-1)

mp.Next()
