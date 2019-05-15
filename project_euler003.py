"""
The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

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

print(prime_factors(600851475143))