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

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2