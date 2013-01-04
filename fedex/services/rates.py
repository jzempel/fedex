# -*- coding: utf-8 -*-
"""
    fedex.services.rates
    ~~~~~~~~~~~~~~~~~~~~

    FedEx rate web services.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService


class RateService(BaseService):
    """Rate service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``13``.
    """

    def __init__(self, configuration, wsdl_version=13):
        super(RateService, self).__init__(configuration, "Rate", wsdl_version,
                "crs")

    def create_package(self):
        """Create a new package object.
        """
        return self.create("RequestedPackageLineItem")

    def create_shipment(self, international=False):
        """Create a new shipment object.

        :param international: Default ``False``. Determines whether to include
            the Estimated Duties and Taxes element.
        """
        ret_val = self.create("RequestedShipment")
        ret_val.RateRequestTypes = None

        if not international:
            del ret_val.EdtRequestType

        return ret_val

    def get_rates(self, shipment, region="US", **kwargs):
        """Get shipment rates.

        :param shipment: Shipment instance to get rates for.
        :param region: Default ``'US'``. FedEx express region code.
        :param kwargs: Additional service keyword arguments.
        """
        kwargs["RequestedShipment"] = shipment
        self.client_detail.Region = region

        return self.call("getRates", **kwargs)
