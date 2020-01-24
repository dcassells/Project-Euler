"""
Q.
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
-------------
Approach:
Use a Sieve of Eratosthenes implementation
-------------
Use:
python project_euler010.py 2000000
"""

import sys

try:
	limit = int(sys.argv[1])
except:
	sys.exit('Please input number after file, e.g. \'python project_euler010.py 2000000\'')

# create set of odd numbers
numbers = set(range(3,limit+1,2))

for number in range(3,int(limit** 0.5) + 1):
	if number not in numbers:
		# number already removed
		continue

	multiple = number
	while multiple < limit:
		multiple += number
		if multiple in numbers:
			# remove multiple
			numbers.remove(multiple)

print(2+sum(numbers))