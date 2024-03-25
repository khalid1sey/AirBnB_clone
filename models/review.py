#!/usr/bin/python3
"""
class Review that inherits from
BaseModel
"""

from models.base_model import BaseModel
from datetime import datetime


class Review(BaseModel):
    """
    class Amenity that inherits from
    BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
