#!/usr/bin/python3
"""Defines a function that checks the exact class of an object."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.
    """
    return type(obj) is a_class
