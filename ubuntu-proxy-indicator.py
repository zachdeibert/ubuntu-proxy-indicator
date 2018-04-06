#!/usr/bin/env python

import gi
import signal

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = "com.github.zachdeibert.ubuntu-proxy-indicator"

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_DIALOG_AUTHENTICATION, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem("Quit")
    item_quit.connect("activate", quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    main()
