#!/usr/bin/env python3

# read data in file
f = open('birds.txt', 'r')
data = f.read()
f.close()

# count number of words
words = data.split(' ')
print('The words in the text are:')
print(words)
num_words = len(words)
print('The number of words is', num_words)

# count number of lines
lines = data.split('\n')
print('The lines in the text are:')
print(lines)
print('The number of lines is', len(lines))
