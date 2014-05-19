# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def uninstall_configlet(portal):
    controlpanel_tool = getToolByName(portal, 'portal_controlpanel')
    controlpanel_tool.unregisterConfiglet('DropdownConfiguration')


def uninstall(context):
    if context.readDataFile('dropdownmenu-uninstall.txt') is None:
        return
    uninstall_configlet(context.getSite())
