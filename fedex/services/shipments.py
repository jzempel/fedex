# -*- coding: utf-8 -*-
"""
    fedex.services.shipments
    ~~~~~~~~~~~~~~~~~~~~~~~~

    FedEx shipment web services.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService


class ShipmentService(BaseService):
    """Shipment service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``12``.
    """

    def __init__(self, configuration, wsdl_version=12):
        super(ShipmentService, self).__init__(configuration, "Ship",
                wsdl_version, "ship")

    def create_address(self):
        """Create a new party address object.
        """
        return self.create("Party")

    def create_deletion_control(self):
        """Create a new deletion control object.
        """
        return self.create("DeletionControlType")

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

    def create_tracking_id(self):
        """Create a new tracking ID object.
        """
        return self.create("TrackingId")

    def delete(self, tracking_id, deletion_control=None, **kwargs):
        """Delete a shipment.

        :param tracking_id: The tracking ID of the shipment to delete.
        :param deletion_control: Default `None`. If not set, deletes all
            packages.
        :param kwargs: Additional service keyword arguments.
        """
        if deletion_control is None and "DeletionControl" not in kwargs:
            deletion_control = self.create_deletion_control()
            kwargs["DeletionControl"] = \
                    deletion_control.DELETE_ALL_PACKAGES

        return self.call("deleteShipment", TrackingId=tracking_id,
                **kwargs)

    def process(self, shipment):
        """Process a shipment.

        :param shipment: The shipment to process.
        """
        return self.call("processShipment", RequestedShipment=shipment)
