# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Car:
    def __init__(self, brand, year, color):
            self.brand = brand
            self.year = year
            self.color = color
            

# TODO: create instances of the class
b1 = Car("BMW", 1986, "red")
b2 = Car("Audi", 2007, "blue")
b3 = Car("Mercedes", 2006, "light-grey")
# print("class ", b1)

print(b1.brand, b1.year, b1.color)
print(b2.brand, b2.year, b2.color)
print(b3.brand, b3.year, b3.color)






# TODO: print the class and property
