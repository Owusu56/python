# What is a Class?
# A class in Python is like a blueprint for creating objects.
# It defines a set of attributes and methods that the created objects will have.
# Think of it as a template for creating multiple instances of a particular type of object.

# Basic Structure
# Here’s a simple example to illustrate:
class MyClass:
    x = 5


# Creating an object
p1 = MyClass()
print(p1.x)
# Output: 5
# In this example, MyClass is a class with a single attribute x. We create an object p1 from this class and
# access its attribute.


# The __init__ Method
# The __init__ method is a special method that gets called when you create an instance of the class.
# It’s used to initialize the object’s attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)  # Output: John
print(p1.age)   # Output: 36


# Methods in Classes
# Classes can also have methods, which are functions defined within the class that operate on the objects
# created from the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + {self.name})

p1 = Person("John", 36)
p1.greet()  # Output: Hello, my name is John





# Classes in Python also support inheritance, allowing for creating new classes that inherit attributes and methods
# from existing classes. This promotes code reusability and allows for creating a hierarchy of classes with varying
# levels of specificity. Inheritance in Python is achieved by specifying the parent class in parentheses after the
# class name.


# Another benefit of using classes in Python is encapsulation. By encapsulating data and functionality within a
# class, developers can hide the implementation details of the class and expose only the necessary interface to
# other parts of the program. This can help improve code organization and reduce the risk of unintentional
# changes to the internal state of the class.


# Another important concept related to classes in Python is polymorphism, which allows for different classes to
# define methods with the same name but with different implementations. This enables objects of different classes
# to be treated interchangeably, so long as they support a common interface. Polymorphism helps to write more
# generic and flexible code by allowing for different implementations to be used depending on the context.

# Summary
# Class: A blueprint for creating objects.
# Object: An instance of a class.
# Attributes: Variables that belong to the class.
# Methods: Functions that belong to the class.
# __init__ method: Initializes the object’s attributes.
# Inheritance: A way to create a new class using details of an existing class.