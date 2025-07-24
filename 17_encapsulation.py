# Encapsulation: Restrict direct access to some components.

class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute (cannot access directly)

    def set_age(self, age):
    # Setter method to modify private attribute
      if age > 0:
        if age < 18:
            print("You are a minor")
        elif age == 18:
            print("You have just become an adult")
        elif age > 18:
            print("You are an adult")
        self.__age = age
      else:
        print("Age must be positive!")


    def get_age(self):
        # Getter method to access private attribute
        return self.__age

# Creating object
person = Person("Amaan", 20)
print(f"Name: {person.name}")
print(f"Age: {person.get_age()}")      # Access age via method

person.set_age(25)                     # Update age using setter
print(f"Updated age: {person.get_age()}")

# Direct access to __age would fail:
# print(person.__age)   # AttributeError!
