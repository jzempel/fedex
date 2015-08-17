# -*- coding: utf-8 -*-
"""
    fedex.services.addresses
    ~~~~~~~~~~~~~~~~~~~~~~~~

    FedEx address web services.

    :copyright: 2014 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService


class AddressService(BaseService):
    """Address service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``4``.
    """

    def __init__(self, configuration, wsdl_version=4):
        super(AddressService, self).__init__(configuration,
                "AddressValidation", wsdl_version, "aval")

    def create_address(self):
        """Create a new address object.
        """
        return self.create("AddressToValidate")

    def validate(self, addresses, **kwargs):
        """Validate a list of addresses.

        :param addresses: A list of addresses to validate.
        :param kwargs: Additional service keyword arguments.
        """
        kwargs["AddressesToValidate"] = addresses

        return self.call("addressValidation", **kwargs)
