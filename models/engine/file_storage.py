#!/usr/bin/python3
"""Class FileStorage: serializes and deserializes instances to JSON file"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Our Filestorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(my_dict, myfile)

    def reload(self):
        """Deserializes the JSON file to __objects
         (only if the JSON file (__file_path)
        exists, otherwise, do nothing. The file contains a dictionary
        in the form key:dict and we need a dictionary in the form key:object"""
        try:
            with open(FileStorage.__file_path, "r") as myfile:
                a_dict = json.load(myfile)

            for key, value in a_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
