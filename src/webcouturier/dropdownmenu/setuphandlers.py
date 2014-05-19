# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def uninstall_configlet(portal):
    controlpanel_tool = getToolByName(portal, 'portal_controlpanel')
    controlpanel_tool.unregisterConfiglet('DropdownConfiguration')


def remove_properties(portal):
    pp = getToolByName(portal, 'portal_properties')
    pp.manage_delObjects(['dropdown_properties'])


def uninstall(context):
    if context.readDataFile('dropdownmenu-uninstall.txt') is None:
        return
    portal = context.getSite()
    uninstall_configlet(portal)
    remove_properties(portal)
