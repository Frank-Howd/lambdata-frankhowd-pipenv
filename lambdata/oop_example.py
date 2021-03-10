"""Object Oriented Programming Examples - Sprint 1 Module 2"""

import pandas as pd 


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]  # Number of cells in df


class BearMinimumClass:  # Upper camel case whenever creating a class
    pass


class Complex:
    def __init__(self, real_part, imag_part):
        # Constructor, it is the initializer of the class object, it constructs
        # our objects; it is typically used to define our attributes
        """
        Constructor for Complex Numbers
        Complex numbers have a real part and an imaginary part
        """
        self.r = real_part
        self.i = imag_part

    def add(self, other_complex):  # add(num2)
        self.r += other_complex.r  # num1.r += num2.r
        self.i += other_complex.i  # num1.i += num2.i

    def __repr__(self):
        return "({}, {})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):  # Constructor method
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100 
        # If upvotes > 100 will return True, is popular - using 'is' in
        # your method name indicates you are looking for a Boolean return
        # 'is_popular'


class Animal():
    """General Representation of Animals"""

    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return "Vroom, Vroom, I go quick"

    def eat(self, food):
        return "Huge fan of that " + food


class Sloth(Animal): 
    # Sloth is the child the inherits everything from it's parent class, Animal
    
    def __init__(self, name, weight, diet_type, num_naps=104):
        super().__init__(name, weight, diet_type)
        self.num_naps = float(num_naps)

    def run(self): # Can override methods from the parent class.
        return "I am a slow guy"

    def say_something(self):
        return "This is a sloth typing"


if __name__ == "__main__": 
    # Wrapping the below in this statement means that the below will only print
    # out if we run/execute the file oop_example.py; it won't print on imports
    num1 = Complex(3, -5)  # num1.r = 3, num1.i = -5
    num2 = Complex(2, 6)  # num2.r = 2, num2.i = 6

    num1.add(num2)
    print("num1.r: {}, num1.i: {}".format(num1.r, num1.i))

    user1 = SocialMediaUser("Frank", 'Vernon, CT', 500)
    user2 = SocialMediaUser("Carl", "Mississippi")
    user3 = SocialMediaUser("George Washington", "Djibouti", 4000)
    user4 = SocialMediaUser("Carlos", "Argentina", 4)

    print(user1.is_popular())
    print(user2.is_popular())
    user2.receive_upvotes(101)
    print("received {} upvotes".format(user2.upvotes))
    print(user2.is_popular())
