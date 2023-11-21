#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__size):
            print("#" * self.__size)