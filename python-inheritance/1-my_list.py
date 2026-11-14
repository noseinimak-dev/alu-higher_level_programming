#!/usr/bin/python3
"""Defines a list class that can print itself sorted."""


class MyList(list):
    """A list that can print itself in ascending order."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
