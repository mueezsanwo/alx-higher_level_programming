#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """this class represent a square"""

    def __init__(self, size=0):
        """initialize a square
        args: size = size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
