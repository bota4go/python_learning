# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Car:
    def __init__(self, brand, year):
            self.brand = brand
            self.year = year
            

# TODO: create instances of the class
b1 = Car("BMW", 1986)
b2 = Car("Audi", 2007)
b3 = Car("Mercedes", 2006)
print("class ", b1)

print(b1.brand, b1.year)
print(b2.brand, b2.year)
print(b3.brand, b3.year)






# TODO: print the class and property
