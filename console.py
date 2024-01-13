#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.cmd):
    """Defines the HolbertonBnB command interpreter.


    Attributes:
        prompt: the command prompt.
    """
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        "User"
    }

    def emptyline(self):
        """Handles empty line."""
        pass

    def do_quit(self, args):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program."""
        raise SystemExit

    def do_create(self, args):
        """Usage: create <class>.
        Create a new class instance and print its id.
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Usage: show<class> <id> or <class>.show(<id>).
        Display the string representation of a class instance of agiven id.
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = FileStorage().all()
        obj = all_objects.get(key)
        if not obj:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, args):
        """Usage: destroy <class> <id> or <class>.destroy(<id>).
        Delete a class instance of a given id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = FileStorage().all()
        obj = all_objects.get(key)
        if not obj:
            print("** no instance found **")
            return
        del all_objects[key]
        FileStorage().save()

    def do_all(self, args):
        """Usage: all or all <class> or <class>.all().
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = args.split()
        all_objects = FileStorage().all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print(HBNBCommand.classes[class_name].all())

    def do_count(self, args):
        """Usage: count <class> or <class>.count().
        Retrieve the number of instances of a given class.
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instances_count = len(HBNBCommand.classes[class_name].all())
        print(instances_count)

    def do_update(self, args):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>).
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return
         if len(args) < 2:
             print("** instance id missing **")
             return
         obj_id = args[1]
         key = "{}.{}".format(class_name, obj_id)
         all_objects = FileStorage().all()
         obj = all_objects.get(key)
         if not obj:
             print("** no instance found **")
             return
         if len(args) < 3:
             print("** attribute name missing **")
             return

         if args[2][0] == '{' and args[-1][-1] == '}':
             try:
                 attr_dict = eval(' '.join(args[2:]))
             except (NameError, SyntaxError):
                 print("** invalid dictionary syntax **")
                 return
             if type(attr_dict) is not dict:
                 print("** not a valid dictionary **")
                 return
             for key, value in attr_dict.items():
                 setattr(obj, key, value)
                 obj.save()
         else:
             attribute_name = args[2]
             if len(args) < 4:
                 print("** value missing **")
                 return
             attribute_value = args[3]
             try:
                 attribute_value = eval(attribute_value)
             except (NameError, SyntaxError):
                 pass
             setattr(obj, attribute_name, attribute_value)
             obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
