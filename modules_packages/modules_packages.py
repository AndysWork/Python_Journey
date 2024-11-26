#import adder
import math # form math import * - Import all, not a good practice
from adder import add
import welcome
import sys
import pandas
import welcome
import importlib
importlib.reload(welcome) #Used for reloading a Module

print(add(23, 34))
print(math.pi)
#print(sys.path) # Environment Paths
print(pandas.__path__)

#Package -> Sub-Package -> Module

