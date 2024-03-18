#!/usr/bin/python3
"""
class Amenity that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class Amenity(BaseModel):
    """
    class Amenity that inherits from
    BaseModel
    """
    name = ""
