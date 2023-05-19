#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    name = ""
    state_id = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
