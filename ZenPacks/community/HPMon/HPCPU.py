################################################################################
#
# This program is part of the HPMon Zenpack for Zenoss.
# Copyright (C) 2008, 2009, 2010, 2011 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""HPCPU

HPCPU is an abstraction of a CPU.

$Id: HPCPU.py,v 1.1 2011/01/04 23:09:20 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from Globals import InitializeClass
from Products.ZenModel.CPU import CPU

class HPCPU(CPU):
    """CPU object"""

    core = 1
    socket = 0
    clockspeed = 0
    extspeed = 0
    voltage = 0
    cacheSizeL1 = 0
    cacheSizeL2 = 0

    _properties = (
         {'id':'core', 'type':'int', 'mode':'w'},
         {'id':'socket', 'type':'int', 'mode':'w'},
         {'id':'clockspeed', 'type':'int', 'mode':'w'},     #MHz
         {'id':'extspeed', 'type':'int', 'mode':'w'},       #MHz
         {'id':'voltage', 'type':'int', 'mode':'w'},        #Millivolts
         {'id':'cacheSizeL1', 'type':'int', 'mode':'w'},    #KBytes
         {'id':'cacheSizeL2', 'type':'int', 'mode':'w'},    #KBytes
    )

InitializeClass(HPCPU)
