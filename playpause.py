#!/usr/bin/python

import dbus
import sys

from subprocess import call

import player

try:
    mp,props = player.getPlayer()
except:
    sys.exit(-1)

status = str(props.Get("org.bluez.MediaPlayer1", "Status"))

if status == 'playing':
    mp.Pause();
else:
    mp.Play();
