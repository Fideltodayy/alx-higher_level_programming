class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__size):
            print("#" * self.__size)