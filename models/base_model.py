#!usr/bin/python3
""" Base  model class that defines all common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """The main base class"""
    def __init__(self, *args, **kwargs):
        """Constructor of each instance. Uses kwargs if not empty"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a  user friendly representationof the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute with current date&time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with  all instance __dict__ keys/values"""
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict.update({"created_at": self.created_at.isoformat()})
        my_dict.update({"updated_at": self.updated_at.isoformat()})
        return (my_dict)
