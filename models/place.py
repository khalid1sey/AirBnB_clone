#!/usr/bin/python3
"""
class Place that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class Place(BaseModel):
    """
    class Amenity that inherits from
    BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
