#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB command"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on end-of-file."""
        return True

    def do_create(self, arg):
        """Create Save JSON file"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            valid_classes = [
                "BaseModel", "User",
                "Place", "State",
                "City", "Amenity",
                "Review"
            ]
            if args[0] not in valid_classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[obj_key])

    def do_destroy(self, arg):
        """
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            valid_classes = [
                "BaseModel", "User",
                "Place", "State",
                "City", "Amenity",
                "Review"
            ]
            if args[0] not in valid_classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[obj_key]
                    storage.save()

    def do_all(self, arg):
        """
        """
        if not arg:
            all_objs = storage.all()
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            valid_classes = [
                "BaseModel", "User",
                "Place", "State",
                "City", "Amenity",
                "Review"
            ]
            try:
                cls_obj = [str(obj) for obj in storage.all(eval(arg)).values()]
                print(cls_obj)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            valid_classes = [
                "BaseModel", "User",
                "Place", "State",
                "City", "Amenity",
                "Review"
            ]
            if args[0] not in valid_classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id miising **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key not in all_objs:
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    instance = all_objs[obj_key]
                    if args[3][0] == '{' and args[3][-1] == '}':
                        try:
                            attrs_dict = eval(args[3])
                            for key, value in attrs_dict.items():
                                setattr(instance, key, vaue)
                        except Exception as e:
                            print("** InCorrect dictionary syntax:", e)
                        else:
                       setattr(instance, args[2], eval(args[3]))
                    instance.save()

    def emptyline(self):
        """Do nothing on empty input lines."""
        pass

    def default(self, line):
        """
        """
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            if args[1].startswith("show(") and args[1].endswith(")"):
                instance_id = args[1][5:-1]
                a = class_name
                b = instance_id
                self.do_show(f"{a} {b}")
            elif args[1].startswith("destroy(") and args[1].endswith(")"):
                instance_id = args[1][8:-1]
                a = class_name
                b = instance_id
                self.do_destroy(f"{a} {b}")
            elif args[1].startswith("update(") and args[1].endswith(")"):
                update_args = args[1][7:-1].split(', ')
                if len(update_args) == 3:
                    instance_id, attr_name, attr_value = update_args
                    a = class_name
                    b = instance_id
                    c = attr_name
                    d = attr_value
                    self.do_update("{a} {b} {c} {d}")
                elif len(update_args) == 2:
                    instance_id, attrs_dict_str = update_args
                    if attrs_dict_str[0] == '{' and attrs_dict_str[-1] == '}':
                        try:
                            attrs_dict = eval(attrs_dict_str)
                            s = attrs_dict.items()
                            attrs_list = [f"{k} {v}" for k, v in s]
                            a = class_name
                            b = instance_id
                            self.do_update(f"{a} {b} {' '.join(attrs_list)}")
                        except Exception as e:
                            print("*** Incorrect dictionary syntax:", e)
                    else:
                        print("*** Incorrect dictionary syntax:", line)
                else:
                    print("*** Incorrect dictionary syntax:", line)
            elif args[1] == "all()":
                self.do_all(class_name)
            elif args[1] == "count()":
                try:
                    count = len(storage.all(eval(class_name)).values())
                    print(count)
                except NameError:
                    print("** class doesn't exist **")
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
