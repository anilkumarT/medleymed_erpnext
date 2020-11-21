# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in feedback_enquiry/__init__.py
from feedback_enquiry import __version__ as version

setup(
	name='feedback_enquiry',
	version=version,
	description='Custom Form',
	author='medley',
	author_email='anil.kumar@medleymed.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
