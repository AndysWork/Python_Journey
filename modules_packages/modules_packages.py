#import adder
import math # form math import * - Import all, not a good practice
import random
from adder import add
import welcome
import sys
import pandas
import welcome
import importlib
importlib.reload(welcome) #Used for reloading a Module
import sports.football.attack as att

test = 'Testing'
print(add(23, 34))
print(math.pi)
#print(sys.path) # Environment Paths
print(pandas.__path__)

#Package -> Sub-Package -> Module

print(att.shoot())

print(dir(test)) #Returns all the available methods in the scope

class SuperMarket:
    def __init__(self, store):
        self.store = store
    
    def customer_name(self):
        customer_name = input('What\'s your name?' )
        print('Welcome to '+self.store+', '+customer_name)
    
    def __dir__(self): #implements dir method
        return ['customer_name', 'store']

user = SuperMarket('Walmart')
print(user.customer_name)
print(dir(user))

#if __name__ == '__main__': #check for specific code execution from base module