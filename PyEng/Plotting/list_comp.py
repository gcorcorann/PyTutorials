#!/usr/bin/env python3
import numpy as np

x = [5,10,15,20,25]
# declare y as an empty list
y = []

# not so good way
for counter in x:
    y.append(counter / 5)

print('\nOld fashioned way: x = {} y = {}\n'.format(x, y))

# pythonic way
z = [n/5 for n in x]
print('List Comprehensions: x = {} z = {}\n'.format(x, z))

# numpy
try:
    a = x / 5
except:
    print("No, you can't do that with regular Python lists\n")

a = np.array(x)
b = a / 5
print('With Numpy: a = {} b = {}\n'.format(a, b))

