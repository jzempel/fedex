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


PY3 = (sys.version_info[0] >= 3)


def install_requires():
    """
    Different install_requires for Python 2 and Python 3
    """
    requirements = ["six==1.8.0"]
    if PY3:
        requirements.append("suds-py3==1.0.0.0")
    else:
        requirements.append("suds==0.4.1")

def dependency_links():
    """
    Different dependency_links for Python 2 and Python 3
    """
    if PY3:
        return []
    return ["https://github.com/nemith/suds/tarball/master#egg=suds-0.4.1"]


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
    install_requires=install_requires(),
    dependency_links=dependency_links(),  # NOQA
    test_suite="fedex.tests"
)

