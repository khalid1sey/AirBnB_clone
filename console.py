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
        print("EOF signal to exit the program")
        
    def do_create(self, arg):
        """Create instance specified by user"""
        
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
        """Print string repr of a class instance, given id"""
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
        """Delete a class instance of a given id, save result to json file"""
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
        """Display count of instances specified"""
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
            
            class_name, method_arg = args
            if method_arg == 'count()':
                self.do_count(class_name)
                return
            elif method_arg == 'create()':
                print(f"*** Unknown syntax: {class_name}.create()")
                return
            elif method_arg.startswith('show(') and method_arg.endswith(')'):
                method_name = "show"
                # Extract the ID from between the parentheses
                id_str = method_arg[5:-1]
                instance_id = method_arg.split('(')[1][:-1]
            
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
                                instance_id = shlex.split(pattern[2])[0].replace(",", "")
                                line += f" {instance_id} {dict}"
                                self.onecmd(line.strip())
                                return
                         
                        except IndexError:
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
            else:
                print("** invalid syntax **")
                return
            self.onecmd(line.strip())
            return    

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = shlex.split(arg)

        objects = storage.all()
        if args:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                for obj in objects.values():
                    if type(obj) is self.valid_classes[class_name]:
                        print(str(obj))
        else:
            print(str([str(obj) for obj in objects.values()]))
       
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if arg == "":
            print("** class name missing **")
            return
        elif re.findall(r"\{.*?\}", arg):
            
            pattr = r'(\w+)?\s?([\da-f-]+)?\s?({.*})?'
            match1 = re.match(pattr, arg)
            if match1:
                class_name = match1.group(1)
                instance_id = match1.group(2)
                dictionary_representation = match1.group(3)

                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():

                    if class_name is None:
                        print("** class name missing **")
                        return
                
                    if class_name not in self.valid_classes:
                        print("** class doesn't exist **")
                        return

                    if class_name and instance_id is None:
                        print("** instance id missing **")
                        return
                    
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return
                    
                obj = storage.all()[key]
                dict = re.findall(r"\{.*?\}", arg)
                
                if dict:
                    dictionary_string = dict[0].strip("'")
                    try:
                        
                        dict_repr = ast.literal_eval(dictionary_string)
                    except (ValueError, SyntaxError):
                        print("** invalid dictionary representation **")
                        return
                
                    #Update instance attributes with the dictionary values
                    for attr_name, attr_value in dict_repr.items():
                        setattr(obj, attr_name, attr_value)
        else:
            patt = r'(\w+)\("([\da-f-]+)"(?:, "(\w+)")?(?:, "(\w+)")?\)'
            patt2 = r"(\w+)?\s?([\da-f-]+)?\s?(\w+)?\s?((\d+\.?\d*)|(\d*\.?\d+)|\"([^\"]*)\"|'([^']*)')?"   
            mach = re.match(patt, arg)
            mach2 = re.match(patt2, arg)
            

            if mach:
                class_name = mach.group(1)
                instance_id = mach.group(2)
                attribute_name = mach.group(3)
                attribute_value = mach.group(4)
                
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
             
                    if class_name is None:
                        print("** class name missing **")
                        return
                
                    if class_name not in self.valid_classes:
                        print("** class doesn't exist **")
                        return

                    if class_name and instance_id is None:
                        print("** instance id missing **")
                        return
                    
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return
                    
                elif key in storage.all():
                    if attribute_name is None and attribute_value is None:
                        print("** attribute name missing **")
                        return
                    elif attribute_name is not None and attribute_value is None:
                        print("** value missing **")
                        return
                    
                attr_name = attribute_name
                attr_value = attribute_value
                obj = storage.all()[key]

                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    pass
                setattr(obj, attr_name, attr_value)
            else:
                if mach2:
                    list_mach = list(mach2.groups())
                    
                    class_name = mach2.group(1)
                    instance_id = mach2.group(2)
                    attribute_name = mach2.group(3)
                    attribute_value = mach2.group(4)
                    
                    key = "{}.{}".format(class_name, instance_id)
                    if key not in storage.all():

                        if class_name is None:
                            print("** class name missing **")
                            return
                    
                        if class_name not in self.valid_classes:
                            print("** class doesn't exist **")
                            return
                        
                        if class_name and instance_id is None:
                            print("** instance id missing **")
                            return
                        
                        if instance_id not in storage.all():
                            print("** no instance found **")
                            return
                    
                    elif key in storage.all():
                        if attribute_name is None and attribute_value is None:
                            print("** attribute name missing **")
                            return
                        elif attribute_name is not None and attribute_value is None:
                            print("** value missing **")
                            return
                    attr_name = attribute_name
                    attr_value = attribute_value
                    obj = storage.all()[key]

                    try:
                        attr_value = eval(attr_value)
                    except (NameError, SyntaxError):
                        pass
                    setattr(obj, attr_name, attr_value)
               
        storage.save()
       
if __name__ == '__main__':
    HBNBCommand().cmdloop()