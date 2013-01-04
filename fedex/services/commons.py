# -*- coding: utf-8 -*-
"""
    fedex.services.commons
    ~~~~~~~~~~~~~~~~~~~~~~

    FedEx web service commons.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from logging import getLogger
from suds.client import Client
import os


class BaseService(object):
    """Base service.

    :param configuration: API configuration.
    :param wsdl_name: The name of the WSDL for this service.
    :param wsdl_version: The WSDL version number.
    :param service_id: The FedEx service ID.
    """

    def __init__(self, configuration, wsdl_name, wsdl_version, service_id):
        name = "{0}Service_v{1:d}.wsdl".format(wsdl_name, wsdl_version)
        wsdl = os.path.join(configuration.wsdls, name)
        self.client = Client(wsdl)
        self.logger = getLogger("fedex")
        credential = self.create("WebAuthenticationCredential")
        credential.Key = configuration.key
        credential.Password = configuration.password
        self.credentials = self.create("WebAuthenticationDetail")
        self.credentials.UserCredential = credential
        self.client_detail = self.create("ClientDetail")
        self.client_detail.AccountNumber = configuration.account_number
        self.client_detail.MeterNumber = configuration.meter_number
        self.version = self.create("VersionId")
        self.version.ServiceId = service_id
        self.version.Major = wsdl_version
        self.version.Intermediate = 0
        self.version.Minor = 0

    def call(self, method, **kwargs):
        """Call the given web service method.

        :param method: The name of the web service operation to call.
        :param kwargs: Method keyword-argument parameters.
        """
        kwargs["ClientDetail"] = self.client_detail
        kwargs["Version"] = self.version
        self.logger.debug("%s(%s)", method, kwargs)
        kwargs["WebAuthenticationDetail"] = self.credentials
        instance = getattr(self.client.service, method)

        return instance(**kwargs)

    def create_transaction(self):
        """Create a new transaction object.
        """
        return self.create("TransactionDetail")

    def create(self, wsdl_type):
        """Create an object of the given WSDL type.

        :param wsdl_type: The WSDL type to create an object for.
        """
        return self.client.factory.create(wsdl_type)
