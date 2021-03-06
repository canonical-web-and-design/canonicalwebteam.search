#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="canonicalwebteam.search",
    version="0.2.1",
    author="Canonical webteam",
    author_email="webteam@canonical.com",
    url="https://github.com/canonical-web-and-design/canonicalwebteam.search",
    description=(
        "Flask extension to provide a search view for querying the webteam's "
        "Google Custom Search account"
    ),
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["Flask>=1.0.2", "canonicalwebteam.http"],
    tests_require=["httpretty"],
)
