#!/usr/bin/python3
"""This module defines a Square class with a size attribute, a position attribute, an area method, and a print method."""


class Square:
    """Represents a square with a size attribute, a position attribute, an area method, and a print method."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a size and a position.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character."""
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0], "#" * self.size, sep="")

    def __str__(self):
        """Returns a string representation of the square."""
        if self.size == 0:
            return ""
        return ("\n" * self.position[1] + "\n".join(" " * self.position[0] + "#" * self.size for _ in range(self.size)))
    