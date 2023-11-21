#!/usr/bin/python3
"""
This module defines a MagicClass that represents a circle.
"""

import math

class MagicClass:
    """
    Represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the circle with a radius.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Returns the circumference of the circle.
        """
        return 2 * math.pi * self.__radius