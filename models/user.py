#!/usr/bin/python3
"""
class User that inherits from
BaseModel
"""

#import uuid
#from datetime import datetime
#import models
from models.base_model import BaseModel

#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class User(BaseModel):
    """
    class User that inherits from
    BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # @classmethod
    # def all(cls):
    #     """Returns a list of all instances of the class."""
    #     from models import storage
    #     return [obj for obj in storage.all().values() if isinstance(obj, cls)]
