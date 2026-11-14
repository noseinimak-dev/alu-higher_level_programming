#!/usr/bin/python3
"""Defines a geometry class with an unimplemented area method."""


class BaseGeometry:
    """Represents the base of all geometry classes."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
