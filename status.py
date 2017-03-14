#!/usr/bin/python

import dbus
import sys

import player

try:
    mp,props = player.getPlayer()
except:
    sys.exit(0)

data = props.Get("org.bluez.MediaPlayer1","Track")

try:
    title  = str(data["Title"])[:40]
except:
    title = "..."
try:
    artist = str(data["Artist"])[:40]
except:
    artist = "..."
try:
    album  = str(data["Album"])[:40]
except:
    album = "..."


if len(title) == 40:
    title = title + "..."

if len(artist) == 40:
    artist = artist + "..."

if len(album) == 40:
    album= album+ "..."

try:
    status  = str(props.Get("org.bluez.MediaPlayer1", "Status"))
except:
    status = "none"

try:
    shuffle = str(props.Get("org.bluez.MediaPlayer1", "Shuffle"))
except:
    shuffle = "none"

try:
    repeat = str(props.Get("org.bluez.MediaPlayer1", "Repeat"))
except:
    repeat = "none"

if status == 'playing':
    icon = "⮓"
elif status == 'none':
    icon = "?"
else:
    icon = "⮔"

if shuffle == 'alltracks':
    shufficon = "⇌"
elif shuffle == 'none':
    shufficon = "?"
else:
    shufficon = "⇀"

if repeat == 'singletrack':
    repeaticon = '1'
else:
    repeaticon = ''

duration = int(data["Duration"]) // 1000
position = int(props.Get("org.bluez.MediaPlayer1", "Position")) // 1000

mins = duration // 60
secs = duration % 60
dur = "{0}:{1:02}".format(mins,secs)

mins = position // 60
secs = position % 60
pos = "{0}:{1:02}".format(mins,secs)

print("{0} {1} [{2}] - {3} | ⮖ {4}/{5} {6} {7}".format(icon, artist, album, title, pos, dur, shufficon, repeaticon))


