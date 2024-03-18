#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models
#from models import storage
#from models.__init__ import storage
#from models.engine.file_storage import storage

class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instantiation of public attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        if key != '__class__':
                            setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        display the string representation of created objects
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime and saves to storage
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
