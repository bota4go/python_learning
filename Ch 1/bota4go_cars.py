# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

from datetime import date
import sys
from tkinter.tix import NoteBook
from termcolor import colored, cprint

# TODO: create a basic class
class Car:
    def __init__(self, brand, year, color, price):
            self.brand = brand
            self.year = year
            self.__PriceYear = 2020
            self.color = color
            self.price = price
    
    #calculate age        
    def age(self):
        return date.today().year-self.year

    #return or calculate price
    def getprice(self):
        if hasattr(self, "_CorrectionPercent"):
            self.price = self.price * self._CorrectionPercent
            return self.price
        else:
            return self.price

    #set correction 
    def setnewprice(self, CorrectionPercent, CorrectionYear):
        self._CorrectionPercent = CorrectionPercent
        self._CorrectionYear = CorrectionYear

    def onscreen(self):
        message = colored('{} it is a brand', 'magenta')
        print(message.format(self.brand), end=' ')
        message = colored('and price is {}', 'yellow')
        print(message.format(self.getprice()), end=colored('$ ','yellow'))
        message = colored('and age is {}', 'green')
        print(message.format(self.age()), end=' ')
        message = colored('and {} it is its color', 'red')
        print(message.format(self.color))
        return 0


class Notebook:
    def __init__(self, Brand, year, price):
        self.Brand = Brand
        self.year = year
        self.price = price



# TODO: create instances of the class
b1 = Car("BMW", 1986, "red", 10000)
b2 = Car("Audi", 2007, "blue", 25000)
b3 = Car("Mercedes", 2006, "light-grey", 5000)

# TODO: print the class and property
b1.onscreen()
b2.onscreen()
b3.onscreen()

b1.setnewprice(0.5, 2022)
message = colored ('Set new price','blue', attrs=['blink', 'reverse'])
print (message)
b1.onscreen()

print ("print secret", b1._Car__PriceYear)

a1 = Notebook("Fujitsu", 2015, 1000)
a2 = Notebook("MAC", 2022, 3500)

print(type(b1))
print(type(a1))

print((type(a1)) == type(b1))
print(isinstance(a1,Car))
print(isinstance(b1,Car))





