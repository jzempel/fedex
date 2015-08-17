#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~

    Setup the fedex distribution.

    :copyright: 2014 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup
import fedex

setup(
    name="fedex.py",
    version=fedex.__version__,
    url="http://github.com/jzempel/fedex",
    license=fedex.__license__,
    author=fedex.__author__,
    author_email="jzempel@gmail.com",
    description="FedEx API for Python.",
    long_description=__doc__,
    packages=["fedex"],
    package_data={"fedex": ["wsdls/*.wsdl"]},
    include_package_data=True,
    install_requires=["suds-jurko"],
    test_suite="fedex.tests"
)
