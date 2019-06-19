"""
Q.
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

-------------
Approach:
Use our prime generator

-------------
Use:
python project_euler007.py 10001
"""
import sys

def prime(i, primes):
	for prime in primes:
		if not (i == prime or i%prime):
			return False
	primes.add(i)
	return i

def primes_gen(n):
	primes = set([2])
	i, p = 2, 0
	while True:
		if prime(i, primes):
			p += 1
			if p == n:
				return primes
		i += 1

print(max(primes_gen(int(sys.argv[1]))))