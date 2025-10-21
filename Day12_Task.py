# Attributes
# Example No.01
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The name of the animal is {self.name}")
        print(f"The age of the animal is {self.age}")

    def sound(self):
        print("The animal makes a sound")

    def move(self):
        print("The animal moves")

    def eat(self):
        print("The animal eats")

    def sleep(self):
        print("The animal sleeps")
obj = animal("Dog", 5)
obj.display()
obj.sound()
obj.move()
obj.eat()
obj.sleep()

# Example No.02
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"The make of the car is {self.make}")
        print(f"The model of the car is {self.model}")
        print(f"The year of the car is {self.year}")

    def start(self):
        print("The car starts")

    def stop(self):
        print("The car stops")

    def accelerate(self):
        print("The car accelerates")

    def brake(self):
        print("The car applies the brakes")

    def turn(self):
        print("The car turns")
car1 = car("Toyota", "Camry", 2022)
car1.display()
car1.start()
car1.stop()
car1.accelerate()
car1.brake()
car1.turn()

# Example No.03
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"The make of the vehicle is {self.make}")
        print(f"The model of the vehicle is {self.model}")
        print(f"The year of the vehicle is {self.year}")

    def start(self):
        print("The vehicle starts")

    def stop(self):
        print("The vehicle stops")

    def accelerate(self):
        print("The vehicle accelerates")

    def brake(self):
        print("The vehicle applies the brakes")

    def turn(self):
        print("The vehicle turns")
vehicle2 = vehicle("Honda", "Civic", 2021)
vehicle2.display()
vehicle2.start()
vehicle2.stop()
vehicle2.brake()
vehicle2.accelerate()
# Example No.04
class parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The name of the parent is {self.name}")
        print(f"The age of the parent is {self.age}")

    def work(self):
        print("The parent works")

    def play(self):
        print("The parent plays")

    def sleep(self):
        print("The parent sleeps")

class child(parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        super().display()
        print(f"The grade of the child is {self.grade}")

    def study(self):
        print("The child studies")

    def play(self):
        print("The child plays")

    def sleep(self):
        print("The child sleeps")

child1 = child("John", 12, "A")
child1.display()
child1.study()
child1.play()
child1.sleep()
# Example No.05
class father:
    def skill():
        print("The father is a skilled carpenter")

class mother:
    def skill():
        print("The mother is a skilled cook")

class child(father, mother):
    def skill():
        print("The child is a skilled artist")
obj = child()
child.skill()
child.skill()
child.skill()

# Example No.06
class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The name of the grandparent is {self.name}")
        print(f"The age of the grandparent is {self.age}")

    def work(self):
        print("The grandparent works")

    def play(self):
        print("The grandparent plays")

    def sleep(self):
        print("The grandparent sleeps")

class Parent(Grandparent):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def display(self):
        super().display()
        print(f"The job of the parent is {self.job}")

    def work(self):
        print("The parent works")

    def play(self):
        print("The parent plays")

    def sleep(self):
        print("The parent sleeps")

class Child(Parent):
    def __init__(self, name, age, job, grade):
        super().__init__(name, age, job)
        self.grade = grade

    def display(self):
        super().display()
        print(f"The grade of the child is {self.grade}")

    def study(self):
        print("The child studies")

    def play(self):
        print("The child plays")

    def sleep(self):
        print("The child sleeps")

child1 = Child("John", 12, "Carpenter", "A")
child1.display()
child1.study()
child1.play()
child1.sleep()


       
