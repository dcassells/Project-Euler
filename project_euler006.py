"""
Q.
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

-------------
Approach:
(1 + 2 + ... + 10)^2 = 1*1 + 1*2 + 1*3 + ... + 2*1 + 2*2 + 2*3 + ... + 10*8 + 10*9 + 10*10
					 = 1*1 + 2*2 + ... + 10*10 + ... + 1*2 + 1*3 + ... + 2*1 + 2*3 + ... + 10*8 + 10*9
					 = (1^2 + 2^2 + ... + 10^2) + 1*2 + 1*3 + ... + 2*1 + 2*3 + ... + 10*8 + 10*9

Hence we need to do a double loop and avoid the squares to find the difference.

We can actually do this in half the time as we get two of each pair.
					 = (1^2 + 2^2 + ... + 10^2) + 1*2 + 1*3 + ... + 2*1 + 2*3 + ... + 10*8 + 10*9
					 = (1^2 + 2^2 + ... + 10^2) + 1*2 + 2*1 + 1*3 + 3*1 + ... + 9*10 + 10*9
					 = (1^2 + 2^2 + ... + 10^2) + 2(1*2) + 2(1*3) + ... + 2(9*10)
"""

import sys

def sum_sq_difference(x):

	difference = 0

	for i in range(1,x+1):
		for j in range(i+1,x+1):
			# print('2*(',i,'*',j,')')
			difference += 2*i*j

	return difference


print(sum_sq_difference(int(sys.argv[1])))

