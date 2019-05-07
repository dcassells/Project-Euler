"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5,
	 we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
"""


def three_multiple(x):
	if x%3 == 0:
		return 1
	else:
		return 0

def five_multiple(x):
	if x%5 == 0:
		return 1
	else:
		return 0

def three_five_multiple_sum(a):
	multi_sum = 0

	for i in range(a):
		if three_multiple(i):
			multi_sum = multi_sum + i
		elif five_multiple(i):
			multi_sum = multi_sum + i

	return multi_sum

print(three_five_multiple_sum(1000))