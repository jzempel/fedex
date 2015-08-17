# -*- coding: utf-8 -*-
"""
    fedex.services
    ~~~~~~~~~~~~~~

    FedEx web services.

    :copyright: 2014 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .addresses import AddressService
from .commons import BaseService
from .rates import RateService
from .shipments import ShipmentService
from .tracking import TrackingService


class FedexService(BaseService):
    """FedEx service wrapper.

    :param configuration: API configuration.
    """

    def __init__(self, configuration):
        self.address_service = AddressService(configuration)
        self.rate_service = RateService(configuration)
        self.shipment_service = ShipmentService(configuration)
        self.tracking_service = TrackingService(configuration)

    def get_addresses(self, addresses, **kwargs):
        """Get a list of addresses.

        :param addresses: A list of addresses to get valid shipping addresses
            for.
        :param kwargs: Additional service keyword arguments.
        """
        return self.address_service.validate(addresses, **kwargs)

    def get_rates(self, shipment, **kwargs):
        """Get shipment rates.

        :param shipment: Shipment instance to get rates for.
        :param kwargs: Additional service keyword arguments.
        """
        return self.rate_service.get_rates(shipment, **kwargs)

    def get_shipment(self, shipment):
        """Get a processed shipment.

        :param shipment: The shipment to process.
        """
        return self.shipment_service.process(shipment)

    def get_tracking(self, selection_details, **kwargs):
        """Get package tracking.

        :param selection_details: Details to select the package to track.
        :param kwargs: Additional service keyword arguments.
        """
        return self.tracking_service.track(selection_details, **kwargs)

    def remove_shipment(self, tracking_id):
        """Remove a processed shipment.

        :param tracking_id: The tracking ID of the shipment to remove.
        """
        return self.shipment_service.delete(tracking_id)
