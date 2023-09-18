#!/usr/bin/python3
""" module doc for rectangle """
from models.base import Base

class Rectangle(Base):
    """ class doc for rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ func doc """
        self.checks(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def check_int(self, attr, val):
        """ func doc """
        if not isinstance(val, int):
            raise TypeError(f"{attr} must be an integer")

    def check_positive(self, attr, val):
        """ func doc """
        if val <= 0:
            raise ValueError(f"{attr} must be > 0")

    def check_positive_zero(self, attr, val):
        """ func doc """
        if val < 0:
            raise ValueError(f"{attr} must be >= 0")

    def checks(self, width, height, x, y):
        """ func doc """
        self.check_int("width", width)
        self.check_int("height", height)
        self.check_int("x", x)
        self.check_int("y", y)
        self.check_positive("width", width)
        self.check_positive("height", height)
        self.check_positive_zero("x", x)
        self.check_positive_zero("y", y)
