# -*- coding: utf-8 -*-
"""
    fedex.services.tracking
    ~~~~~~~~~~~~~~~~~~~~~~~

    FedEx tracking web services.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .commons import BaseService


class TrackingService(BaseService):
    """Tracking service.

    :param configuration: API configuration.
    :param wsdl_version: Default ``6``.
    """

    def __init__(self, configuration, wsdl_version=6):
        super(TrackingService, self).__init__(configuration, "Track",
                wsdl_version, "trck")

    def create_package_id(self):
        """Create a new package ID object.
        """
        return self.create("TrackPackageIdentifier")

    def track(self, package_id, **kwargs):
        """Track a package.

        :param package_id: ID of the package to track.
        :param kwargs: Additional service keyword arguments.
        """
        kwargs["PackageIdentifier"] = package_id

        return self.call("track", **kwargs)
