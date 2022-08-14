# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

from datetime import date
import sys
from tkinter.tix import NoteBook
from turtle import clear
from termcolor import colored, cprint
import os
from time import sleep

# TODO: create a basic class
class Car:
    CAR_TYPES = ("Collection", "Regular")

    __carlist = None

    #access to method without definition an instance? 
    @classmethod
    def getcartypes(cls):
        return cls.CAR_TYPES

    #access to method without definition an instance? 
    #doesnot midify?
    @staticmethod
    def getcarlist():
        if Car.__carlist == None:
            Car.__carlist = []
        return Car.__carlist    

    def __init__(self, car_type, brand, year, color, price):
            self.brand = brand
            self.year = year
            self.__PriceYear = 2020
            self.color = color
            self.price = price
            if (not car_type in Car.CAR_TYPES):
                raise ValueError (f"bota4go, {car_type}  is not a valid car type")
            else:
                 self.car_type =car_type

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

    # print on screen
    def onscreen(self):
        message = colored('{} it is a brand', 'magenta')
        print(message.format(self.brand), end=' ')
        message = colored('and price is {}', 'yellow')
        print(message.format(self.getprice()), end=colored('$ ','yellow'))
        message = colored('and age is {}', 'green')
        print(message.format(self.age()), end=' ')
        message = colored('and {} it is its color', 'red')
        print(message.format(self.color))
        return 'done'


class Notebook:
    def __init__(self, Brand, year, price):
        self.Brand = Brand
        self.year = year
        self.price = price



# TODO: create instances of the class
os.system('cls')

c = [Car]
c[0] = Car("Collection", "BMW", 1986, "red", 10000)
c.append(Car)
c[1] = Car("Collection","Audi", 2007, "blue", 25000)
c.append(Car)
c[2] = Car("Regular","Mercedes", 2006, "light-grey", 5000)

# TODO: print the class and property

print("Numbers of data", len(c))

for x in c:
    reply=x.onscreen()
    print(reply)
    

#processes the data

c[0].setnewprice(0.5, 2022)
message = colored ('Set new price','blue', attrs=['blink', 'reverse'])
print (message)
c[0].onscreen()

# print ("print secret", c[0]._Car__PriceYear)

a1 = Notebook("Fujitsu", 2015, 1000)
a2 = Notebook("MAC", 2022, 3500)

print ("Car types: ", Car.getcartypes())

thecarlist = Car.getcarlist()
thecarlist.append(c[0])
thecarlist.append(c[1])
print(thecarlist)

# print(type(c[0]))
# print(type(c))
# print(type(a1))
# print((type(a1)) == type(c[0]))
# print(isinstance(a1,Car))
# print(isinstance(c[0],Car))
# print("os name is :", os.name)
# sleep(2)
# os.system('cls')






