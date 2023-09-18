#!/usr/bin/python3
""" module doc for base """
import json


class Base:
    """ class doc """
    __nb_objects = 0

    def __init__(self, id=None):
        """ func doc """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
