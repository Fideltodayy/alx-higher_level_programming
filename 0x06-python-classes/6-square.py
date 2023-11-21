#!/usr/bin/python3
"""This module defines a Square class with a size attribute, an area method, a print method, size getter and setter, and a class method."""


class Square:
    """Represents a square with a size attribute, an area method, a print method, size getter and setter, and a class method."""

    def __init__(self, size):
        """
        Initializes the square with a size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character."""
        for _ in range(self.__size):
            print("#" * self.__size)

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """Returns the bigger square or the first one if they are equal."""
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
