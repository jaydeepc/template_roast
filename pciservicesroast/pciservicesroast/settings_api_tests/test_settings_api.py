from cafe.drivers.unittest.decorators import tags
from pciservicesroast.fixture import PCIServicesAPIFixture
import unittest2 as unittest

class SettingsAPITests(PCIServicesAPIFixture):

    def test_settings_data_get_status(self):
        status_entity = self.settings_api_client.settings_data_status_get()
        self.assertEquals(status_entity.status_code, 200,
                            msg="Status code does not match. Actual status code found was : {0} instead of Expected \
                            status code: {1}".format(status_entity.status_code, 200))
        status_entity = status_entity.entity
        self.assertIsNotNone(status_entity.data_from, msg="DataFrom attribute is not getting populated")
        self.assertIsNotNone(status_entity.data_to, msg="DataTo attribute is not getting populated")
        self.assertIsNotNone(status_entity.last_update, msg="LastUpdate attribute is not getting populated")
        self.assertIsNotNone(status_entity.next_update, msg="NextUpdate attribute is not getting populated")
        self.assertIsNotNone(status_entity.transactions, msg="Transactions attribute is not getting populated")
        self.assertIsNotNone(status_entity.version, msg="version attribute is not getting populated")

    @tags(type="test")
    def test_settings_data_get_status_by_id(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")

    @tags(type="test")
    def test_settings_data_get_status_by_invalid_id(self):
        a = self.notifications_api_client.get_all_notifications()
        self.assertEquals(1,2, msg="Values do not match")