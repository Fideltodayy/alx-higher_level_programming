#!/usr/bin/python3
"""Defines a Python class-to-JSON method/func."""


def class_to_json(obj):
    """Return the dict representation of a simple data structure."""
    return obj.__dict__
