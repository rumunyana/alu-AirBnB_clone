#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
