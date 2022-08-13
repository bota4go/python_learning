# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

from datetime import date
import sys
from termcolor import colored, cprint

# TODO: create a basic class
class Car:
    def __init__(self, brand, year, color, priceUSD):
            self.brand = brand
            self.year = year
            self.color = color
            self.priceUSD = priceUSD
            
    def age(self):
        return date.today().year-self.year


def onscreen(a):
  message = colored('{} it is a brand', 'magenta')
  print(message.format(a.brand), end=' ')
  message = colored('and price is {}', 'yellow')
  print(message.format(a.priceUSD), end=colored('$ ','yellow'))
  message = colored('and age is {}', 'green')
  print(message.format(a.age()), end=' ')
  message = colored('and {} it is its color', 'red')
  print(message.format(a.color))
  return 0



# TODO: create instances of the class
b1 = Car("BMW", 1986, "red", 10000)
b2 = Car("Audi", 2007, "blue", 25000)
b3 = Car("Mercedes", 2006, "light-grey", 5000)

onscreen(b1)
onscreen(b2)
onscreen(b3)



# print(b1.brand, b1.year, b1.color, b1.priceUSD, "USD")
# print(b2.brand, b2.year, b2.color, b2.priceUSD, "USD")
# print(b3.brand, b3.year, b3.color, b3.priceUSD, "USD")

# message = '{} it is a brand'
# print(message.format(b1.brand), end=' ')
# message = 'and price is {}'
# print(message.format(b1.priceUSD))

# print(b1.age())
# print(b2.age())
# print(b3.age())





# TODO: print the class and property
