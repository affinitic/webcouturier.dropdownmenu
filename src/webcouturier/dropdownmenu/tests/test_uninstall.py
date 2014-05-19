# -*- coding: utf-8 -*-
import unittest2 as unittest
from Products.CMFCore.utils import getToolByName
from plone.app.testing import applyProfile
from webcouturier.dropdownmenu.tests.layer import DROPDOWNMENU_INTEGRATION


class TestUninstall(unittest.TestCase):

    layer = DROPDOWNMENU_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']
        applyProfile(self.portal, 'webcouturier.dropdownmenu:uninstall')

    def test_browserlayer(self):
        from plone.browserlayer import utils
        from webcouturier.dropdownmenu.browser.interfaces import IDropdownSpecific
        self.assertFalse(
            IDropdownSpecific in utils.registered_layers())

    def test_jsregistry(self):
        cssreg = getToolByName(self.portal, 'portal_javascripts')
        js_ids = cssreg.getResourceIds()
        self.assertFalse(
            '++resource++dropdown-menu.js' in
            js_ids)

    def test_cssregistry(self):
        cssreg = getToolByName(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertFalse(
            'dropdown-menu.css' in
            stylesheets_ids)
        self.assertFalse(
            '++resource++dropdown-menu.css' in
            stylesheets_ids)

    def test_controlpanelaction(self):
        controlpanel = getToolByName(self.portal, "portal_controlpanel")
        actions_ids = [action.getId() for action in controlpanel.listActions()]
        self.assertFalse('DropdownConfiguration' in actions_ids)

    def test_properties_uninstall(self):
        ptool = self.portal.portal_properties
        self.assertEquals(ptool.get('dropdown_properties', None), None)

    def test_skins(self):
        stool = self.portal.portal_skins
        skins = stool.objectIds()
        self.assertFalse('dropdownmenu' in skins)
        self.assertFalse('dropdownmenu_sunburst' in skins)
