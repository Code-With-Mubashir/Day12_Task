# What are the attributes?
Attributes refer to variables or methods that are associated with an object (which is an instance of a class).Attributes define the state and behavior of an object.
## 1.Instance Attributes
These are attributes unique to each object(instance) of a class. They are usually defined inside the _init_method.
## 2.Class Attributes
Class attributes are variables that are shared among all instances of a class. They are defined directly inside the class body, but outside of any instance methods like _init_.
They are used when you want all instances of the class to have the same value for a particular attributes, unless explicitly overridden.
## 3.Accessing Attributes
Accessing attributes means retrieving the value of an attributes (either instance or class) from an object or class using dot notation.
# What is Method?
In python, a method is a function that is defined inside a class and is associated with an object (or class). It describes the behavior of an object.
## 1._init_Method
The __init__()  method is a special method in python classes –- also called the constructor.
It is automatically called when you create (instantiate) a new object from a class.
It initializes the object with specific values (i.e., sets up instance attributes).
It’s not required, but commonly used.
## 2.Self Parameter
In python, self is a conventionally used name for the first parameter of instance methods in a class. It refers to the current object (instance) that the method is being called on.
Think of self as how the object refers to itself.
## Why is self-needed?
Python passes the instance (object) automatically to instance methods, but you still have to define self explicitly as the first parameter.
It lets you:
-	Access or modify instance attributes.
-	Call other methods from the same object.
## String Representation
String Representation refers to how an object is displayed as a string –especially when you:
-	Use print(object)
-	Use str(object) or repr(object)
-	View the object in a debugger or interpreter
Python provides two special methods that define how an object is represented as a string.
-	__string__(self)
-	__repr__(self)
## Deleting Objects
In python, you can delete objects manually using the del statement, but in most cases, Python handles object deletion automatically through garbage collection.
## 1.Using del to Delete an Object
The del statement removes a reference to an object. If no more references exist, the object is garbage collected.
## 2.Object Destruction with __del__()
Python classes can define a special method called ___del___ () –this is the destructor, called when an object is about to be destroyed.
#Instance Variables
Instance variables are specific to each object. They are defined using self and typically set in the ___init__ () method.
# Class Variables
Class variables are shared across all instances of the class. You define them directly in the class body, outside any method.
#Inheritance
Inheritance is a powerful concept that allows one class to inherit attributes and methods from another.
## 1.Single Inheritance
A class inherits from one parent class.
## 2.Multiple Inheritance
A class inherits from two or more parent class.
## 3.Multilevel Inheritance
Inheritance that forms a chain: A class inherits from a class that already inherits from another class.
