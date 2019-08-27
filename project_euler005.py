"""
Q.
2520 is the smallest number that can be divided by each of the numbers
	from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
	of the numbers from 1 to 20?

Approach:
Find the union of prime factors

Use:
python project_euler005.py 20

This code needs some improvements to make it more robust.
However, it answers the stated problem.
"""

import sys
from collections import Counter

def prime(i,primes):
	for prime in primes:
		if not (i%prime):
			return False
	primes.add(i)
	return i

def prime_factors(x):
	# set of primes
	primes = set()
	# initiate iterator
	i = 2
	# prime factors
	factors = list()

	while True:

		if prime(i,primes):
			while True:
				# if x = 1 then we are done
				if x == 1:
					return factors

				# check if i is a factor
				elif x%i == 0:	
					# append new prime factor
					factors.append(i)
					# update x
					x = x/i

				# else move on to the next prime
				else:
					break

		# increment iterator
		i += 1

def prime_factor_union(x):

	checked = list()

	factors_union = Counter()

	p_factors = prime_factors(x)

	for n in p_factors:
		factors_union[n] += 1

	checked.append(x)

	for i in reversed(range(2,x)):
		
		not_checked_factor = True

		for j in checked:
			
			if not (j%i):
				
				not_checked_factor = False
				break
				
		if not_checked_factor:
			
			test_factors = Counter()

			p_factors = prime_factors(i)

			for n in p_factors:
				test_factors[n] += 1

			factors_union = factors_union | test_factors

		checked.append(i)

	return factors_union


prime_factor_union = prime_factor_union(int(sys.argv[1]))

even_divisible = 1

for item in prime_factor_union.items():

	even_divisible = even_divisible * (item[0]**item[1])


print(even_divisible)