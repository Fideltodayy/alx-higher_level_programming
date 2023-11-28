#!/usr/bin/python3
"""Defines a Rectangle class with validation checks."""

class Rectangle:
    """Represent a rectangle with validation for width and height."""
    def __init__(self, width, height):
        if isinstance(width, int) and width > 0:
            self.width = width
        else:
            raise ValueError("Width must be a positive integer")
        if isinstance(height, int) and height > 0:
            self.height = height
        else:
            raise ValueError("Height must be a positive integer")
        