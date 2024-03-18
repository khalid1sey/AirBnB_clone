#!/usr/bin/python3
"""
class Review that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class Review(BaseModel):
    """
    class Amenity that inherits from
    BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
