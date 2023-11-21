#!/usr/bin/python3
"""This module defines a Square class with a size attribute, an area method, a print method, and size getter and setter."""


class Square:
    """Represents a square with a size attribute, an area method, a print method, and size getter and setter."""

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