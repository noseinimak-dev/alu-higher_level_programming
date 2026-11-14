#!/usr/bin/python3
"""Defines a function that checks if an object is of a kind of class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to compare with.
    """
    return isinstance(obj, a_class)
