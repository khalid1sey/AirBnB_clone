#!/usr/bin/python3
"""
class State that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class State(BaseModel):
    """
    class State that inherits from
    BaseModel
    """
    name = ""
