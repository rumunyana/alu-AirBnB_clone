#!/usr/bin/python3
"""file storage"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    __file_path = "./file.json"
    __objects = {}
    """instantiate file storage"""

    def __init__(self):
        pass

    """return the dictionary"""

    def all(self):
        return self.__objects

    """add new dictionary"""

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    """save __objects json in a file"""

    def save(self):
        objs = {}
        for key in self.__objects.keys():
            objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objs, file)

    """get dict from file"""

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key in data.keys():
                    cls = classes[data[key]["__class__"]]
                    obj = cls(**data[key])
                    self.new(obj)
                return data
        except FileNotFoundError:
            pass
