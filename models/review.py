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

    def __init__(self, *args, **kwargs):
            """Initialize Review instance."""
            super().__init__(*args, **kwargs)

    def save(self):
        """Update the updated_at attribute and save."""
        self.updated_at = datetime.now()
        super().save()  # Call save method of the BaseModel class