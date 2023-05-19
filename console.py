#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def do_help(self, arg):
        super().do_help(arg)

    def help_help(self):
        print("help command to provide more information")

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            model = classes[arg]()
            storage.save()
            print(model.id)

    def help_create(self):
        print("Create command to create a new object")

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            arr = arg.split(" ")
            if arr[0] not in classes.keys():
                print("** class doesn't exist **")
            elif len(arr) < 2:
                print("** instance id missing **")
            else:
                all_items = storage.all()
                item = all_items.get("{}.{}".format(arr[0], arr[1]))
                if not item:
                    print("** no instance found **")
                else:
                    print(item)

    def help_show(self):
        print("Show command to display a single \
        object by providing a type and Id")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            arr = arg.split(" ")
            if arr[0] not in classes.keys():
                print("** class doesn't exist **")
            elif len(arr) < 2:
                print("** instance id missing **")
            else:
                all_items = storage.all()
                item = all_items.get("{}.{}".format(arr[0], arr[1]))
                if not item:
                    print("** no instance found **")
                else:
                    del all_items["{}.{}".format(arr[0], arr[1])]
                    storage.save()

    def help_destroy(self):
        print(
            "Destroy command to delete a \
            single object. the object type and id are needed")

    def do_all(self, arg):
        if not arg:
            items = storage.all()
            arr = [str(items[i]) for i in items.keys()]
            print(arr)
        else:
            if arg not in classes.keys():
                print("** class doesn't exist **")
            else:
                items = storage.all()
                arr = [str(items[i]) for i in items.keys()
                       if items[i].__class__.__name__ == arg]
                print(arr)

    def help_all(self):
        print("all command to get all \
        the object in our application")

    def do_update(self, arg):
        arr = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif arr[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            items = storage.all()
            item = items.get("{}.{}".format(arr[0], arr[1]))
            if not item:
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
            elif len(arr) < 4:
                print("** value missing **")
            else:
                setattr(item, arr[2], arr[3])
                storage.save()

    def help_update(self):
        print("update command to \
        update the a single object property")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
