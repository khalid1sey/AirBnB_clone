#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


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
                    date_format = '%Y-%m-%dT%H:%M:%S.%f'
                    try:
                        parsed_date = datetime.strptime(value, date_format)
                    except ValueError:
                        raise ValueError("Invalid isoformat string")
                    parsed_date = datetime.strptime(value, date_format)
                    setattr(self, key, parsed_date)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            current_time = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def __str__(self):
        """
        display the string representation of created objects
        """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self) -> None:
        """
        updates the public instance attribute updated_at \
            with the current datetime and saves to storage
        """
        self.updated_at = datetime.now()
        # from models import storage  # Import here to avoid circular import
        models.storage.save()
        # storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values \
            of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
