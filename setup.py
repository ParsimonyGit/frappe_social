# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_social/__init__.py
from frappe_social import __version__ as version

setup(
	name="frappe_social",
	version=version,
	description="Frappe v13 application for the 'Social Wall' feature that was removed in v12",
	author="Parsimony LLC",
	author_email="developers@parsimony.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
