#!/usr/bin/python3
""" module doc for square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class doc for square """

    def __init__(self, size, x=0, y=0, id=None):
        """ func doc """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ func doc """
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"
