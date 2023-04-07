#!/usr/bin/python3
""" defination of a class called  square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes square
        Args:
        size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of square and return the result as a square
        """

        return self.__size ** 2
