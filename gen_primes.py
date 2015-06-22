#!/usr/bin/env python
import sys

@profile
def prime_list(num):

    primes = []
    for x in xrange(2, num + 1):
        is_prime = True
        for y in xrange(2, int(x ** 0.5) + 1):
            if x % y == 0:  # if y is a factor of x
                is_prime = False
                break  # no need to check the rest
        if is_prime:
            primes.append(x)
    return primes


if __name__ == '__main__':
    print prime_list(int(sys.argv[1]))
