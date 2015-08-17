# -*- coding: utf-8 -*-
"""
    fedex.services.tracking
    ~~~~~~~~~~~~~~~~~~~~~~~

    FedEx tracking web services.

    :copyright: 2014 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService


class TrackingService(BaseService):
    """Tracking service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``10``.
    """

    def __init__(self, configuration, wsdl_version=10):
        super(TrackingService, self).__init__(configuration, "Track",
                wsdl_version, "trck")

    def create_selection_details(self):
        """Create a new selection details object.
        """
        return self.create("TrackSelectionDetail")

    def track(self, selection_details, **kwargs):
        """Track a package.

        :param selection_details: Details to select the package to track.
        :param kwargs: Additional service keyword arguments.
        """
        kwargs["SelectionDetails"] = selection_details

        return self.call("track", **kwargs)
