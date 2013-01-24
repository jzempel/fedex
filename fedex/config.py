# -*- coding: utf-8 -*-
"""
    fedex.config
    ~~~~~~~~~~~~

    FedEx configuration.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from ConfigParser import NoOptionError, NoSectionError, SafeConfigParser
import os


class FedexConfiguration(object):
    """FedEx service configuration.

    :param integration_id: Unique ID, provided by FedEx, that represents
        your application.
    :param username: FedEx account username.
    :param password: FedEx password.
    :param wsdls: Default `None`. WSDL path URI. Pass ``'beta'`` to use test
        server WSDLs.
    :param file_name: Default `None`. Optional configuration file name.
    :param section: Default ``'default'``. The configuration section to use.
    """

    def __init__(self, key=None, password=None, account_number=None,
            meter_number=None, wsdls=None, file_name=None, section="default"):
        parser = SafeConfigParser()

        if file_name:
            parser.read([file_name])
        else:
            parser.read([os.path.expanduser("~/.fedex.cfg")])

        self.key = self.__get(parser, section, "key", key)
        self.password = self.__get(parser, section, "password", password)
        self.account_number = self.__get(parser, section, "account_number",
                account_number)
        self.meter_number = self.__get(parser, section, "meter_number",
                meter_number)
        self.wsdls = self.__get(parser, section, "wsdls", wsdls)

        if self.wsdls is None or wsdls == "beta":
            file_path = os.path.abspath(__file__)
            directory_path = os.path.dirname(file_path)
            wsdls_path = os.path.join(directory_path, "wsdls")

            if wsdls == "beta":
                wsdls_path = os.path.join(wsdls_path, "beta")

            self.wsdls = "file://{0}".format(wsdls_path)

        assert self.key
        assert self.password
        assert self.account_number
        assert self.meter_number
        assert self.wsdls

    @staticmethod
    def __get(parser, section, name, default):
        """Get a configuration value for the named section.

        :param parser: The configuration parser.
        :param section: The section for the given name.
        :param name: The name of the value to retrieve.
        """
        if default:
            vars = {name: default}
        else:
            vars = None

        try:
            ret_val = parser.get(section, name, vars=vars)
        except (NoSectionError, NoOptionError):
            ret_val = default

        return ret_val
