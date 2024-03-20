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
            # print("{} {}".format("args =", args))
            class_name, method_arg = args
            if method_arg == 'count()':
                self.do_count(class_name)
                return
            elif method_arg.startswith('show(') and method_arg.endswith(')'):
                method_name = "show"
                # Extract the ID from between the parentheses
                id_str = method_arg[5:-1]
                instance_id = method_arg.split('(')[1][:-1]
                # print("{} {}".format("id_str =", id_str))
                # print("{} {}".format("args =", args))
                # print("{} {}".format("class_name =", class_name))
                # print("{} {}".format("method_name =", method_name))
                # print("{} {}".format("instance_id =", instance_id))


            
                arg_str = "{} {}".format(class_name, id_str)
                self.do_show(arg_str)
                return
            elif method_arg == "all()":
             
                self.do_all(class_name)
                return
            elif method_arg.startswith('destroy(') and method_arg.endswith(')'):
                instance_id = method_arg.split('(')[1][:-1]
                self.do_destroy(f"{class_name} {instance_id}")
                return
            elif re.match(r"(\w+)\.(\w+)\((.*)\)", line):
         
                pattern = list(re.match(r"(\w+)\.(\w+)\((.*)\)", line).groups())
                print("{} {}".format("pattern =", pattern))
                # Eliminate empty lines in the returned pattern
                if pattern[-1] == "":
                    pattern.pop()

                if pattern:
                    if len(pattern) >= 2:
                        class_name, method = pattern[0], pattern[1]
                        line = f"{method} {class_name}"

                        try:
                            dict = re.findall(r"\{.*?\}", pattern[2])[0]

                            if method == "update" and dict:
                                dict = eval(dict)
                                # print("{} {}".format("dict after eval=", dict))
                                instance_id = shlex.split(pattern[2])[0].replace(",", "")
                                # print("{} {}".format("instance_id after =", instance_id))
                                line += f" {instance_id} {dict}"
                                # print("{} {}".format("line at end of try block b4 onecmd =", line))
                                # print("{} {}".format("line at end of try block after strip b4 onecmd =", line.strip()))
                                self.onecmd(line.strip())
                                #self.do_update(f"{class_name} {instance_id} {dict}")
                                return
                         
                        except IndexError:
                            #print("** instance id missing **")
                            pass

                        # Check if there is a list and retain it if it exists
                        if len(pattern) >= 3:
                            list_info = re.findall(r"\[.*\]", pattern[2])
                            if list_info:
                                pattern[2] = pattern[2].replace(str(list_info[0]), "")

                        try:
                            more_arg = shlex.split(pattern[2])
                            line += " "
                            line += " ".join(more_arg).replace(",", "")
                            line += f" {list_info or ''}"
                        except (ValueError, IndexError):
                            pass
            self.onecmd(line.strip())
            return    

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        # print("Inside do_all")
        args = shlex.split(arg)
        # print("{} {}".format("arg =", arg))
        # print("{} {}".format("args =", args))
       

        objects = storage.all()
        if args:
            class_name = args[0]
            # print("{} {}".format("class_name =", class_name))
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                for obj in objects.values():
                    if type(obj) is self.valid_classes[class_name]:
                        print(str(obj))
                    # else:
                    #     print("** class doesn't exist **")
        else:
            print(str([str(obj) for obj in objects.values()]))
       
    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        # print("{} {}".format("arg in do_update =", arg))
        dict = re.findall(r"\{.*?\}", arg)
        # print("{} {}".format("dict in do_update =", dict))
        # print("{} {}".format("arg[2] in do_update =", arg[2]))
        
        pattern = r"(.*)"
        match = re.match(pattern, arg)
        # print("{} {}".format("match in do_update =", match))
        instance_id_match = re.search(r'\b[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}\b', match.group(1))
        # print("{} {}".format("instance_id_match =", instance_id_match))
        if not instance_id_match:
            print("** instance id missing **")
            return
        args = shlex.split(arg)
        # print("{} {}".format("args in do_update =", args))
        models = storage.all()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(args[0], args[1])
        # print("{} {}".format("key =", key))
        # print("{} {}".format("storage.all() =", storage.all()))
        if key not in storage.all():
        
            print("** no instance found **")
            return

        obj = storage.all()[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # Extract and parse the dictionary representation using ast.literal_eval
        # print("{} {}".format("args[2:] =", args[2:]))
        
        if dict:
            # print("{} {}".format("dict before try block =", dict))
            dictionary_string = dict[0].strip("'")
            try:
                
                dict_repr = ast.literal_eval(dictionary_string)
                # print("{} {}".format("dict_repr before exception =", dict_repr))
            except (ValueError, SyntaxError):
                print("** invalid dictionary representation **")
                return
        
            #Update instance attributes with the dictionary values
            for attr_name, attr_value in dict_repr.items():
                setattr(obj, attr_name, attr_value)
        else:
            # If the third argument is an attribute name and fourth argument is a value
          
            if len(args) < 4:
                print("** value missing **")
                return

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
