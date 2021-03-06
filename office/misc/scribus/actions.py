#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
    
def setup():
  
    pisitools.dosed("CMakeLists.txt", "\"share\/doc\/\$\{MAIN_DIR_NAME\}.*", "\"share/doc/${MAIN_DIR_NAME}/\")")
    
    cmaketools.configure("-DWANT_DISTROBUILD=YES \
                          -DWANT_QT5SUPPORT=ON")

def build():
    
    cmaketools.make()

def install():
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/share/applications", "scribus.desktop")
    pisitools.insinto("/usr/share/pixmaps", "resources/iconsets/1_5_1/scribus.png")
    pisitools.insinto("/usr/share/pixmaps", "resources/iconsets/1_5_0/scribusdoc.png", "x-scribus.png")
