#!/usr/bin/env python3

# read data in file
f = open('birds.txt', 'r')
data = f.read()
f.close()

lines = data.split('\n')
print('Wrong: The number of lines is', len(lines))

# remove empty lines
for l in lines:
    if not l:
        lines.remove(l)
print('Right: The number of lines is', len(lines))
