################################################################################
#
# This program is part of the HPMon Zenpack for Zenoss.
# Copyright (C) 2008-2012 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""cpqDaCntlr

cpqDaCntlr is an abstraction of a HP Smart Array Controller.

$Id: cpqDaCntlr.py,v 1.5 2012/11/02 18:36:44 egor Exp $"""

__version__ = "$Revision: 1.5 $"[11:-2]

import inspect
from HPExpansionCard import HPExpansionCard
from HPComponent import *

class cpqDaCntlr(HPExpansionCard):
    """Disk Aray Controller object"""

    portal_type = meta_type = 'ExpansionCard'

    FWRev = ""
    role = 1
    redundancyType = ""
    __ifindex = "1"

    # we monitor RAID Controllers
    monitor = True

    statusmap ={1: (DOT_GREY, SEV_WARNING, 'other'),
                2: (DOT_GREEN, SEV_CLEAN, 'Ok'),
                3: (DOT_ORANGE, SEV_ERROR, 'Degraded'),
                4: (DOT_RED, SEV_CRITICAL, 'Failed'),
                }

    _properties = HPExpansionCard._properties + (
        {'id':'FWRev', 'type':'string', 'mode':'w'},
        {'id':'role', 'type':'int', 'mode':'w'},
        {'id':'redundancyType', 'type':'string', 'mode':'w'},
    )


    factory_type_information = (
        {
            'id'             : 'cpqDaCntlr',
            'meta_type'      : 'cpqDaCntlr',
            'description'    : """Arbitrary device grouping class""",
            'icon'           : 'ExpansionCard_icon.gif',
            'product'        : 'ZenModel',
            'factory'        : 'manage_addCpqDaCntlr',
            'immediate_view' : 'viewCpqDaCntlr',
            'actions'        :
            (
                { 'id'            : 'status'
                , 'name'          : 'Status'
                , 'action'        : 'viewCpqDaCntlr'
                , 'permissions'   : (ZEN_VIEW,)
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_DEVICE, )
                },
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW_MODIFICATIONS,)
                },
            )
          },
        )

    def roleString(self):
        roles = {1: 'other',
                2: 'Not Duplexed',
                3: 'Active',
                4: 'Backup',
                }
        return roles.get(self.role, roles[1])

    def getRRDTemplates(self):
        templates = []
        tnames = ['cpqDaCntlr', 'cpqDaAccelCntlr', 'cpqDaCntlrPerf']
        for tname in tnames:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

    def _getSnmpIndex(self):
        frm = inspect.currentframe(2)
        ifindex = ''
        try:
            if frm.f_locals.get('oid','').startswith('1.3.6.1.4.1.232.3.2.7.1'):
                ifindex = '.' + self.__ifindex
        finally:
            del frm
        return self.snmpindex + ifindex

    def _setSnmpIndex(self, value):
        self.__ifindex = value

    ifindex = property(fget=lambda self: self._getSnmpIndex(),
                        fset=lambda self, v: self._setSnmpIndex(v)
                        )

InitializeClass(cpqDaCntlr)
