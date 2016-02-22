from cafe.drivers.unittest.decorators import tags
from pciservicesroast.fixture import PCIServicesAPIFixture

import unittest2 as unittest

class NotificationsAPITests(PCIServicesAPIFixture):

    @tags(type="test")
    def test_get_all_notifications(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")

    @tags(type="test")
    def test_get_all_notifications_marked(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,1, msg="Values do not match")

    @tags(type="test")
    def test_get_notifications_marked_read_by_id(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")

    @tags(type="test")
    def test_get_notifications_marked_read_by_invalid_id(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")

    @tags(type="test")
    def test_get_notifications_marked_read_by_unknown_id(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")