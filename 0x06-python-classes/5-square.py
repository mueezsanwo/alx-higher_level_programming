#!/usr/bin/python3
"""class Square that defines a square."""


class Square:
    """this class represent a square"""

    def __init__(self, size=0):
        """initialize a square
        args: size = size of square"""
        self.size = size

    @property   # Getter
    def size(self):
        """get the size of the square"""
        return (self.__size)

    @size.setter  # Setter
    def size(self, value):
        """set and validate the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

        if self.__size == 0:
            print("")
