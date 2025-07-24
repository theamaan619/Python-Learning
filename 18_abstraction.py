# Abstraction: Define a generic class/interface, hiding complexity.

from abc import ABC, abstractmethod

class Shape(ABC):             # Abstract base class
    @abstractmethod
    def area(self):
        pass                  # Subclasses must override this method

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Usage:
rect = Rectangle(4, 5)
print("Rectangle area:", rect.area())
circ = Circle(3)
print("Circle area:", circ.area())
