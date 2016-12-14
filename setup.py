#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: setup.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
A helpful decorator for choice fields (Django choices or SQLAlchemy ChoiceType)
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
f = path.join(here, 'README.md')

try:
    from pypandoc import convert
    long_description = convert(f, 'rst')
except ImportError:
    print(
        "pypandoc module not found, could not convert Markdown to RST")
    long_description = open(f, 'r').read()

setup(
    name='orm-choices',
    version='0.2.1',
    description=(
        "A helpful decorator for choice fields"
        " (Django choices or SQLAlchemy ChoiceType)"),
    long_description=long_description,
    url='https://github.com/dhilipsiva/orm-choices',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='django orm sqlalchemy choices',
    packages=find_packages(),
    py_modules=['orm_choices'],
    entry_points='''''',
    install_requires=[],
    extras_require={
        'dev': [''],
        'test': [''],
    },
)
