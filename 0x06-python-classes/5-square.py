#!/usr/bin/python3
"""Defination of  a class Square"""


class Square:
    """Represents a square
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
        size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """ square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter __size
        value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
