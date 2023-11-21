#!/usr/bin/python3
"""This module defines a Square class with a size attribute and an area method."""


class Square:
    """Represents a square with a size attribute and an area method."""

    def __init__(self, size):
        """
        Initializes the square with a size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2