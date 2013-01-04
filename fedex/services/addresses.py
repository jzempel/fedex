# -*- coding: utf-8 -*-
"""
    fedex.services.addresses
    ~~~~~~~~~~~~~~~~~~~~~~~~

    FedEx address web services.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService
from datetime import datetime


class AddressService(BaseService):
    """Address service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``2``.
    """

    def __init__(self, configuration, wsdl_version=2):
        super(AddressService, self).__init__(configuration,
                "AddressValidation", wsdl_version, "aval")

    def create_address(self):
        """Create a new address object.
        """
        return self.create("AddressToValidate")

    def create_options(self):
        """Create a new address validation options object.
        """
        return self.create("AddressValidationOptions")

    def validate(self, addresses, options=None):
        """Validate a list of addresses.

        :param addresses: A list of addresses to validate.
        :param options: Default `None`. Address validation options.
        """
        return self.call("addressValidation", RequestTimestamp=datetime.now(),
                AddressesToValidate=addresses, Options=options)
