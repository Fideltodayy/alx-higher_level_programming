#!/usr/bin/python3
"""This module defines a Square class with a size attribute, an area method, and comparison operators."""


class Square:
    """Represents a square with a size attribute, an area method, and comparison operators."""

    def __init__(self, size=0):
        """
        Initializes the square with a size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if this square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if this square is not equal to another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if this square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square is less than or equal to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if this square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square is greater than or equal to another square."""
        return self.area() >= other.area()
