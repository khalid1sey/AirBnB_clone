import json
from models.base_model import BaseModel  # Import BaseModel
from models.user import User  # Import User class
from models.place import Place  # Import the Place class
from models.state import State  # Import the State class
from models.city import City  # Import the City class
from models.amenity import Amenity  # Import the Amenity class
from models.review import Review  # Import the Review class


class FileStorage:
    """
    Serializes instances to a JSON file \
            and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            # if key != f"{obj.__class__.__name__}.{obj.id}":
            #     raise KeyError("invalid key. key must be <class name>.<id>")
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects \
                (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t \
                exist, no exception should be raised).
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    self.__objects[key] = self.valid_classes[class_name](
                        **value
                    )
        except FileNotFoundError:
            pass
