#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project."""
import cmd
import shlex
import ast
import re
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

    # def parse_line(self, line):
    #     # Split the line by '.' and '(' to get the class name, method name, and arguments
    #     parts = line.split('.', 1)
    #     print("{} {}".format("parts =", parts))
    #     if len(parts) == 2:
    #         class_name, rest = parts
    #         if rest.startswith("show(") and rest.endswith(")"):
    #             method_name = "show"
    #             # Extract the ID from between the parentheses
    #             id_str = rest[5:-1]
    #             print("{} {}".format("id_str =", id_str))
    #             print("{} {}".format("parts =", parts))
    #             print("{} {}".format("class_name =", class_name))
    #             print("{} {}".format("method_name =", method_name))
    #             return method_name, class_name, id_str
    #         elif rest == "all()":
    #             self.do_all(rest)
    #     return super().parse_line(line)
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
    
    def do_count(self, arg):
        """Counts the number of instances of a class."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        count = sum(1 for obj in storage.all().values() if isinstance(obj, self.valid_classes[args[0]]))
        print(count)

    def default(self, line):
        args = line.split('.', 1)
        if len(args) == 2:
            print("{} {}".format("args =", args))
            class_name, method_arg = args
            if method_arg == 'count()':
                self.do_count(class_name)
                return
            elif method_arg.startswith('show(') and method_arg.endswith(')'):
                method_name = "show"
                # Extract the ID from between the parentheses
                id_str = method_arg[5:-1]
                instance_id = method_arg.split('(')[1][:-1]
                print("{} {}".format("id_str =", id_str))
                print("{} {}".format("args =", args))
                print("{} {}".format("class_name =", class_name))
                print("{} {}".format("method_name =", method_name))
                print("{} {}".format("instance_id =", instance_id))


                # return method_name, class_name, id_str
                #arg_str = "{} {}".format(class_name, args)
                arg_str = "{} {}".format(class_name, id_str)
                self.do_show(arg_str)
                return
            elif method_arg == "all()":
                #method_name = "all"
                self.do_all(class_name)
                return
            elif method_arg.startswith('destroy(') and method_arg.endswith(')'):
                instance_id = method_arg.split('(')[1][:-1]
                self.do_destroy(f"{class_name} {instance_id}")
                return
            
            # elif method_arg.startswith('update(') and method_arg.endswith(')'):
            #     # Extract instance ID and attribute information using regular expressions
            #     match = re.match(r'update\("(.*?)",\s*({.*})\)', method_arg)
            #     if match:
            #         instance_id = match.group(1)
            #         attribute_info = match.group(2)
            #         print("Instance ID:", instance_id)
            #         print("Attribute info:", attribute_info)
            #         # Call your do_update method with the extracted instance ID and attribute information
            #         self.do_update(f"{class_name} {instance_id} {attribute_info}")
            #         return
                # else:
                #     print("** Invalid update format **")
                #     return

        # super().default(line)
            # elif method_arg.startswith('update(') and method_arg.endswith(')'):
            # # Extract instance ID and attribute information
            #     method_arg = method_arg[7:-1]  # Remove "update(" and ")"
            #     instance_id = None
            #     attribute_info = ""
            #     inside_braces = False
            #     for i, char in enumerate(method_arg):
            #         if char == '{':
            #             inside_braces = True
            #         elif char == '}':
            #             inside_braces = False
            #         elif char == ',' and not inside_braces:
            #             instance_id = method_arg[:i].strip()
            #             attribute_info = method_arg[i + 1:].strip()
            #             break

            #     if instance_id is None or attribute_info == "":
            #         print("** invalid update format **")
            #         return

            #         print("Instance ID:", instance_id)
            #         print("Attribute info:", attribute_info)
            #         # Call your do_update method with the extracted instance ID and attribute information
            #         self.do_update(f"{class_name} {instance_id} {attribute_info}")
            #         return

    # super().default(line)
            elif method_arg.startswith('update(') and method_arg.endswith(')'):
                # Extracting instance id and attribute information from method_arg
                instance_id, attribute_info = method_arg.split('(')[1][:-1].split(',', 1)
                attribute_info = attribute_info.strip()
                if attribute_info.startswith('{') and attribute_info.endswith('}'):
                    print("{} {}".format("instance_id =", instance_id))
                    print("{} {}".format("attribute_info =", attribute_info))
                    # Update with dictionary representation
                    print("Hello")
                    try:
                        # Parse the dictionary representation into a Python dictionary
                        attr_dict = eval(attribute_info)
                        #print("{} {}".format("args[2] =", args[2]))
                        print("{} {}".format("attr_dict =", attr_dict))
                    except (NameError, SyntaxError):
                        print("** invalid dictionary representation **")
                        return

                    #Update instance attributes with the dictionary values
                    #for attr_name, attr_value in attr_dict.items():
                        #setattr(obj, attr_name, attr_value)

                    self.do_update(f"{class_name} {instance_id} {attribute_info}")
                else:
                    # Update with attribute name and value
                    attribute_name, attribute_value = attribute_info.split(',', 1)
                    attribute_name = attribute_name.strip()
                    attribute_value = attribute_value.strip()
                    self.do_update(f"{class_name} {instance_id} {attribute_name} {attribute_value}")
                return
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
            print(str([str(obj) for obj in objects.values()]))
       
    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        print("{} {}".format("arg =", arg))
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

        obj = storage.all()[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # Extract and parse the dictionary representation using ast.literal_eval
        print("{} {}".format("args[2:] =", args[2:]))
        dict_repr = "{'Five': 5, 'Six': '6'}"
        dict_obj = ast.literal_eval(dict_repr)
        print("{} {}".format("dict_repr (hardcode) =", dict_repr))
        #dict_repr = " ".join(args[2:])
        dict_repr = args[-1]
        if dict_repr.startswith('{') and dict_repr.endswith('}'):
            print("World")
            #dict_repr = " ".join(args[2:])
            print("{} {}".format("dict_repr =", dict_repr))
            print("{} {}".format("dict_repr[0] =", dict_repr[0]))
            print("{} {}".format("dict_repr[1] =", dict_repr[1]))
            print("{} {}".format("dict_repr[2] =", dict_repr[2]))
            print("{} {}".format("dict_repr[5] =", dict_repr[5]))
            print("{} {}".format("args[2] =", args[2]))
            # attr_dict = ast.literal_eval(dict_repr)
            # print("{} {}".format("attr_dict1 =", attr_dict))
            print("{} {}".format("dict_repr before try block =", dict_repr))
            try:
                print("Hurray")
                attr_dict = ast.literal_eval(dict_repr)
                #attr_dict = eval(dict_repr)
                #print("{} {}".format("args[2] =", args[2]))
                print("{} {}".format("attr_dict =", attr_dict))
                # for attr_name, attr_value in attr_dict.items():
                #     setattr(obj, attr_name, attr_value)
                print("{} {}".format("dict_repr before exception =", dict_repr))
            except (ValueError, SyntaxError):
                #pass
                print("** invalid dictionary representation **")
                return
        

            #Update instance attributes with the dictionary values
            for attr_name, attr_value in attr_dict.items():
                setattr(obj, attr_name, attr_value)
        else:
            # If the third argument is an attribute name and fourth argument is a value
            print("{} {}".format("args =", args))
            print("{} {}".format("args[0] =", args[0]))
            print("{} {}".format("args[1] =", args[1]))
            print("{} {}".format("args[2] =", args[2]))
            print("Holiday")
            if len(args) < 4:
                print("** value missing **")
                return

            #instance = models[key]
            attr_name = args[2]
            attr_value = args[3]

            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            setattr(obj, attr_name, attr_value)

        storage.save()
       
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
