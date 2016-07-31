# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mischief',
    version='0.0.1',
    description='Utilities for Twitter',
    long_description=readme,
    author='Murtaza Zaidi',
    author_email='murtazazaidi@outlook.com',
    url='https://github.com/murtazazaidi/mischief',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
