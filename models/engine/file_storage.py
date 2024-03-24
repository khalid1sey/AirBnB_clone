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
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
        # print("File path in FileStorage: ", self.__file_path)

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
                    if '.' in key:
                        class_name, obj_id = key.split('.')
                    else:
                        # If key does not contain a period, use the whole key as class_name
                        class_name = key
                        obj_id = value.get('id')
                    class_obj = None
                    if class_name == 'BaseModel':
                        class_obj = BaseModel
                    elif class_name == 'User':
                        class_obj = User
                    else:
                        class_obj = globals()[class_name]

                    self.__objects[key] = class_obj(**value)
    
        except FileNotFoundError:
            pass
