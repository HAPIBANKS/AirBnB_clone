#!/usr/bin/python3
"""
a class Basemodel that defines all common
attributes and methods for other classes
"""


from uuid import uuid4
import models
from datetime import datetime, date, time


class BaseModel:
    """parent class for other classes in
    the Airbnb clone project and it has the following attributes and methods:
    Attributes:
        id: handles user's identity
        created_at: assign with the current datetime when an
                    instance is created
        updated_at: assign with the current datetime when an
                    instance is created and it will be
                    updated every every time the object is changed.
    Methods:
        __str__: print class name
        save(self): update the public instance attribute with
                    current time
        to_dict(self): returns a dictionary containing all
                       keys/value of __dict__.
    """

    def __init__(self, *args, **kwargs):
        """
        Public instance attributes initialization.
        """
        TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """returns string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        update the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.utc()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys and values of __dict__.
        """
        objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                objects[key] = value.isoformat()
            else:
                objects[key] = value
            objects["__class__"] = self.__class__.__name__
            return objects
