#!/usr/bin/python3
"""
Defining  a class called Rectangle
"""


class Rectangle:
    """Represents of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting  the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting  the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returning the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
