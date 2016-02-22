from cafe.drivers.unittest.fixtures import BaseTestFixture

from pciservicescafe.pciservicesapi.config import MarshallingConfig, PCIServicesAPIConfig, PCIAuthConfig
from pciservicescafe.pciservicesapi.settings_api.client import PCIServicesAPIClient
from pciservicescafe.pciservicesapi.notification_api.client import NotificationServicsClient
from pciservicescafe.auth.config import PCIAuthConfig
from pciservicescafe.pciservicesapi.auth_api.client import PCIAuthClient


class PCIServicesAPIFixture(BaseTestFixture):
    """
    @summary: Fixture for any StackTach test.
    """
    @classmethod
    def setUpClass(cls):
        super(PCIServicesAPIFixture, cls).setUpClass()
        cls.marshalling = MarshallingConfig()
        cls.pciservices_config = PCIServicesAPIConfig()
        cls.auth_config = PCIAuthConfig()

        cls.url = cls.pciservices_config.url
        cls.serializer = cls.marshalling.serializer
        cls.deserializer = cls.marshalling.deserializer

        cls.username = cls.auth_config.username
        cls.password = cls.auth_config.password
        cls.authentication_endpoint = cls.auth_config.authentication_endpoint

        cls.auth_client = PCIAuthClient(cls.url, cls.serializer, cls.deserializer)
        cls.token_id = cls.auth_client.get_token(cls.username, cls.password).entity.ID


        cls.settings_api_client = PCIServicesAPIClient(cls.url, cls.token_id, cls.serializer, cls.deserializer)
        cls.notifications_api_client = NotificationServicsClient(cls.url, cls.token_id, cls.serializer, cls.deserializer)