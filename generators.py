#!/usr/bin/env python3
"""
How and Why You Should Use Generators.

@author:    Gary Corcoran
@date_created:  Dec. 8th, 2017

Reference:
https://medium.freecodecamp.org/how-and-why-you-should-use-python-generators-
f6fb56650888
"""

### ITERATORS ##
class PrimesIt:
    """
    Iterator of prime numbers up to ``max_number`` using iterator class.
    """
    def __init__(self, max_number):
        self.max = max_number
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()

## GENERATORS ##
def PrimesGen(max_number):
    """
    Iterator of prime numbers up to ``max_number`` using generator function.
    """
    number = 1
    while number < max_number:
        number += 1
        if check_prime(number):
            yield number

def check_prime(number):
    """
    Checks if number is prime.
    """
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return False
    return True

def main():
    """ Main Function. """
    # Iterator
    primes = PrimesIt(100)
    print(primes)
    for x in primes:
        print(x)

    # Gerneator
    primes = PrimesGen(100)
    print(primes)
    for x in primes:
        print(x)

    # Generator Expression
    primes = (i for i in range(2, 100) if check_prime(i))
    print(primes)
    for x in primes:
        print(x)

if __name__ == '__main__':
    main()
