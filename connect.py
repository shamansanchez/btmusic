#!/usr/bin/python

import dbus
import sys

import player

try:
    dev = player.getDevice()
except:
    sys.exit(-1)

dev.Connect()
