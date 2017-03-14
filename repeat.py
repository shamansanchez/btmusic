#!/usr/bin/python

import dbus
import sys

import player

try:
    mp,props = player.getPlayer()
except:
    sys.exit(-1)

status = str(props.Get("org.bluez.MediaPlayer1", "Repeat"))

if status == 'singletrack':
    props.Set("org.bluez.MediaPlayer1","Repeat","alltracks")
else:
    props.Set("org.bluez.MediaPlayer1","Repeat","singletrack")
