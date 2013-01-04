# -*- coding: utf-8 -*-
"""
    fedex.config
    ~~~~~~~~~~~~

    FedEx configuration.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

import os


class FedexConfiguration(object):
    """FedEx service configuration.

    :param integration_id: Unique ID, provided by FedEx, that represents
        your application.
    :param username: FedEx account username.
    :param password: FedEx password.
    :param wsdls: Default `None`. WSDL path URI. Use ``'beta'`` to use test
        server WSDLs.
    """

    def __init__(self, key, password, account_number, meter_number,
            wsdls=None):
        self.key = key
        self.password = password
        self.account_number = account_number
        self.meter_number = meter_number

        if wsdls is None or wsdls == "beta":
            file_path = os.path.abspath(__file__)
            directory_path = os.path.dirname(file_path)
            wsdls_path = os.path.join(directory_path, "wsdls")

            if wsdls == "beta":
                wsdls_path = os.path.join(wsdls_path, "beta")

            self.wsdls = "file://{0}".format(wsdls_path)
        else:
            self.wsdls = wsdls
