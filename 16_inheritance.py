# Inheritance allows a class to inherit methods and attributes from another class

class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print("Meow")

c = Cat()
c.speak()         # Calls Cat's speak
