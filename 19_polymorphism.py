# Polymorphism: Same interface (method name) can mean different things for different objects.

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Duck:
    def speak(self):
        print("Quack!")

def make_it_talk(animal):
    # We can pass any object with a speak() method!
    animal.speak()

# Usage:
dog = Dog()
cat = Cat()
duck = Duck()

make_it_talk(dog)   # Output: Woof!
make_it_talk(cat)   # Output: Meow!
make_it_talk(duck)  # Output: Quack!
