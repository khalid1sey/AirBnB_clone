#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project."""
import cmd
import shlex
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB Clone project."""

    prompt = "(hbnb) "
    valid_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def help_quit(self):
        """Print help for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help for EOF command."""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{arg}()")
        new_instance.save()
        print(new_instance.id)

    def parse_line(self, line):
        # Split the line by '.' and '(' to get the class name, method name, and arguments
        parts = line.split('.', 1)
        print("{} {}".format("parts =", parts))
        if len(parts) == 2:
            class_name, rest = parts
            if rest.startswith("show(") and rest.endswith(")"):
                method_name = "show"
                # Extract the ID from between the parentheses
                id_str = rest[5:-1]
                return method_name, class_name, id_str
        return super().parse_line(line)
        #args = line.split('.')

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def default(self, line):
        method_name, class_name, args = self.parse_line(line)
        if method_name == "show":
            self.do_show(class_name, args)

        #args = line.split('.')
        print(line)
        print(args)
        #if len(args) == 2:
         #   if args[1].startswith("show(") and args[1].endswith(")"):
          #      id_str = args[1][5:-1] # Extract ID from between parentheses
           #     self.do_show(args[0], id_str)
            #elif args[1] == "all()":
        if len(args) == 2 and args[1] == "all()":
                self.do_all(args[0])
            #else:
             #   super().default(line)
        #elif len(args) == 2 and args[1] == "show(":
            #self.do_show(args[0])
        else:
            super().default(line)

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        print("Inside do_all")
        args = shlex.split(arg)
        print("{} {}".format("arg =", arg))
        print("{} {}".format("args =", args))
        #print(args[0])
        #print(args[1])
        #print(args[2])
        #print(args[3])

        objects = storage.all()
        if args:
            if args[0] in self.valid_classes:
                for obj in objects.values():
                    if type(obj) is self.valid_classes[args[0]]:
                    #if isinstance(obj, self.valid_classes[args[0]]):
                        print(str(obj))
        else:
            print([str(obj) for obj in objects.values()])
        #if not args:
        #if args is []:
            #print([str(obj) for obj in objects.values()])
        #elif args[0] in self.valid_classes and len(args) >= 2 and args[1] == "all()" and hasattr(self.valid_classes[args[0]], "all"):
            #print([str(obj) for obj in self.valid_classes[args[0]].all()])
        #elif args[0] == "all":
            #print([str(obj) for obj in objects.values()])
        #elif len(args) >= 2 and args[1] == ".all()":
            #class_name = args[0]
            #if class_name in self.valid_classes:
                 #print([str(obj) for obj in objects.values() if type(obj).__name__ == class_name])

        #if args[2] in self.valid_classes:
            #print("{}".format(args[0]))
            #print([str(obj) for obj in objects.values() if type(obj).__name__ == args[0]])
            #else:
                #print("** class doesn't exist **")
        #else:
         #   print("** Unknown syntax: {} **".format(arg))
    #def do_all(self, model_name: str) -> None:
     #   """Prints the string representation for all or some model instances."""
        #if model_name and shlex.split(model_name)[0] not in self.__models:
      #  if model_name and shlex.split(model_name)[0] not in self.__valid_classes:
       #     print("** class doesn't exist **")
        #    return

        #objects = storage.all()
       # instances = []

        # print the instances for a specific model, if provided
       # if model_name:
           # for obj in objects.values():
          #      if obj.__class__.__name__ == model_name:
         #           instances.append(str(obj))
        #else:
            # print all the instances available
          #  for obj in objects.values():
         #       instances.append(str(obj))

        #print(instances)
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        models = storage.all()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
        #if key not in models:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        #instance = models[key]
        attr_name = args[2]
        attr_value = args[3]

        #if hasattr(obj, attr_name):
            #setattr(obj, attr_name, eval(attr_value))
            #storage.save()
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
            #print("** attribute doesn't exist **")
        setattr(obj, attr_name, attr_value)
        storage.save()
        #else:
            #print("** attribute doesn't exist **")

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
