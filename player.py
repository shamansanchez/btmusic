#!/usr/bin/python

import dbus
import sys

def getPlayer():
    bus = dbus.SystemBus()
    om = dbus.Interface(bus.get_object("org.bluez", "/"),
                            "org.freedesktop.DBus.ObjectManager")

    objects = om.GetManagedObjects()

    playerpath = None

    for path in objects.keys():
        interfaces = objects[path]
        for interface in interfaces.keys():
            if interface == "org.bluez.MediaPlayer1":
                playerpath = path
                break

    try:
        mp = dbus.Interface(bus.get_object("org.bluez", playerpath),
                            "org.bluez.MediaPlayer1")

        props = dbus.Interface(bus.get_object("org.bluez", playerpath),
                            "org.freedesktop.DBus.Properties")

        return (mp,props)

    except:
        return None

def getDevice():
    bus = dbus.SystemBus()

    # Change to the bluetooth address of your phone
    devpath = "/org/bluez/hci0/dev_DE_AD_BE_EF_CA_FE"

    try:
        dev = dbus.Interface(bus.get_object("org.bluez", devpath),
                            "org.bluez.Device1")

        return dev

    except:
        return None
