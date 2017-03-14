#!/usr/bin/python

import dbus
import sys

import player

try:
    mp,props = player.getPlayer()
except:
    sys.exit(-1)

status = str(props.Get("org.bluez.MediaPlayer1", "Shuffle"))

if status == 'alltracks':
    props.Set("org.bluez.MediaPlayer1","Shuffle","off")
else:
    props.Set("org.bluez.MediaPlayer1","Shuffle","alltracks")
