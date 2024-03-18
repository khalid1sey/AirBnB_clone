#!/usr/bin/python3
"""
class City that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class City(BaseModel):
    """
    class City that inherits from
    BaseModel
    """
    state_id = ""
    name = ""
