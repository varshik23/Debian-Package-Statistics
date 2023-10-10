"""
`setup.py` - Packaging Configuration for the Debian Package Statistics (dps) Module

This script defines the packaging configuration for the Debian Package Statistics (dps) module.
It uses setuptools, a Python package management tool, to package and distribute the module.
"""
from setuptools import setup, find_packages

setup(
    name='dps',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "dps=dps.__main__:main",
        ],
    },
)
