#!/usr/bin/python3
"""
module for a class file_storage that serializes instances to a JSON
file and deserializes JSON file to instances
"""


import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """
    file storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, object):
        """
        sets in __object the obj with key
        <obj class name>.id
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        does not exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as file:
                dict = json.loads(file.read())
                for value in dict.values():
                    cl = value["__class__"]
                    self.new(eval(cl)(**value))
        except Exception:
            pass
