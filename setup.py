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
import sys

install_requires = ["six==1.8.0"]
dependency_links = []

if sys.version_info[0] < 3:
    install_requires.append("suds==0.4.1")
    dependency_links.append("https://github.com/nemith/suds/tarball/master#egg=suds-0.4.1")  # NOQA
else:
    install_requires.append("suds-py3==1.0.0.0")
    dependency_links.append("https://github.com/cackharot/suds-py3/tarball/master#egg=suds-py3-1.0.0.0")  # NOQA

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
    install_requires=install_requires,
    dependency_links=dependency_links,
    test_suite="fedex.tests"
)
