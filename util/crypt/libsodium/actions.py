#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    #shelltools.cd("make/linux")
    autotools.make("PREFIX=/usr")

def install():
    #shelltools.cd("make/linux")
    autotools.install("libdir=%s/usr/lib" % get.installDIR())

    pisitools.dodoc("ChangeLog", "LICENSE","README.*")
