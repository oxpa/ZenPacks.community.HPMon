################################################################################
#
# This program is part of the HPMon Zenpack for Zenoss.
# Copyright (C) 2008, 2009, 2010, 2011 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""HPFan

HPFan is an abstraction of a fan or probe.

$Id: HPFan.py,v 1.2 2011/01/04 23:11:37 egor Exp $"""

__version__ = "$Revision: 1.2 $"[11:-2]

from Products.ZenModel.Fan import Fan
from HPComponent import HPComponent

class HPFan(Fan, HPComponent):
    """Fan object"""

    status = 1

    _properties = Fan._properties + (
                 {'id':'status', 'type':'int', 'mode':'w'},
                 )

    def state(self):
        return self.statusString()

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

InitializeClass(HPFan)