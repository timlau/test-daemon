#!/usr/bin/python3
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

# (C) 2013-2014 Tim Lauridsen <timlau@fedoraproject.org>

#
# Test system bus dBus service
#
from gi.repository import Gtk

import argparse
import dbus
import dbus.service
import dbus.mainloop.glib
import logging

DAEMON_ORG = 'dk.yumex.Test'
DAEMON_INTERFACE = DAEMON_ORG
logger = logging.getLogger(DAEMON_ORG)



class TestDaemon(dbus.service.Object):

    def __init__(self):
        dbus.service.Object.__init__(self)
        bus_name = dbus.service.BusName(DAEMON_ORG, bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, '/')

#=========================================================================
# DBus Methods
#=========================================================================

    @dbus.service.method(DAEMON_INTERFACE,
                         in_signature='',
                         out_signature='i')
    def GetVersion(self):
        """
        Get the daemon version
        """
        return 100

    @dbus.service.method(DAEMON_INTERFACE,
                         in_signature='',
                         out_signature='b',
                         sender_keyword='sender')
    def Exit(self, sender=None):
        """
        Exit the daemon
        :param sender:
        """
        Gtk.main_quit()
        return True

def main():
    parser = argparse.ArgumentParser(description='Test D-Bus Daemon')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('--notimeout', action='store_true')
    args = parser.parse_args()
    # setup the DBus mainloop
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    yd = TestDaemon()
    Gtk.main()


if __name__ == '__main__':
    main()
