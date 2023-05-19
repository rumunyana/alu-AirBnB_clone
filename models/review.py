#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    text = ""
    place_id = ""
    user_id = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
