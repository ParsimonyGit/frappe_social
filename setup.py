# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_social/__init__.py
from frappe_social import __version__ as version

setup(
	name="frappe_social",
	version=version,
	description="App to contain social wall feature of frappe version 12 that works with frappe version-13",
	author="Diksha Jadhav",
	author_email="dikshajadhav11.dj@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
