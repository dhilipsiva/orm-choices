#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: choices.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-11-26
"""

import inspect


def user_attributes(klass):
    defaults = dir(type('defaults', (object,), {}))  # gives all inbuilt attrs
    return [
        item[0]
        for item in inspect.getmembers(klass)
        if item[0] not in defaults]


def choices(klass):
    """
    Decorator to set `CHOICES` and other attributes
    """
    _choices = []
    for attr in user_attributes(klass.Meta):
        val = getattr(klass.Meta, attr)
        setattr(klass, attr, val[0])
        _choices.append((val[0], val[1]))
    setattr(klass, 'CHOICES', tuple(_choices))
    return klass


def choices_with_unknown(klass):
    """
    Also add an `UNKNOWN` attribute to the class (Value for unknown: -1)
    """
    klass.Meta.UNKNOWN = [-1, "Unknown"]
    return choices(klass)


def is_valid_choice(klass, value):
    for kv in klass.CHOICES:
        if kv[0] == value:
            return True
    return False
