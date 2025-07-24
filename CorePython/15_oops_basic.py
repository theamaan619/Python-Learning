# Object-Oriented Programming: create classes and objects

class Dog:
    # Constructor (called automatically when object is created)
    def __init__(self, name):
        self.name = name  # Attribute

    # Instance Method
    def bark(self):
        print(self.name, "says Woof!")

    # Destructor (called when object is about to be destroyed)
    def __del__(self):
        print(self.name, "is being deleted")

# Creating an object (instantiation)
my_dog = Dog("Buddy")

# Calling a method
my_dog.bark()

# Deleting the object manually (optional, usually Python's garbage collector handles this)
del my_dog
