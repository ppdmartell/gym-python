# There are three ways to import modules: generic imports, function imports and universal imports

# generic import
import random

# function import
from random import random as random_float # named changed to avoid collision

# universal import
from sys import *

print(random.randint(1, 10))
print(random_float())
