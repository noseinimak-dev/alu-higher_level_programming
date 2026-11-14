#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Objects that are exactly an instance of a_class do not count.

    Args:
        obj: The object to check.
        a_class: The class to compare with.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
