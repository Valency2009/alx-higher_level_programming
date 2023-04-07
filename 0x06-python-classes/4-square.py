#!/usr/bin/python3
"""Defination of a class called  Square"""


class Square:
    """Represents a square in an Attributes
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns None
        """
        self._size = size

    def area(self):
        """calculating  the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """to get __size
        Returns:
            Size of the square
        """
        return self.__size

    @property.setter
    def size(self, value):
        """setting  of __size
        Args:
            value (int): the size of a size of the square
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
