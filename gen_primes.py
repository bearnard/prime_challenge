#!/usr/bin/env python
import sys


def prime_list(num):

    primes = []
    for x in xrange(2, num + 1):
        is_prime = True
        for y in xrange(2, x):
            if x % y == 0:  # if y is a factor of x
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes


if __name__ == '__main__':
    print prime_list(int(sys.argv[1]))
