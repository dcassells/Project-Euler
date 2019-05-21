"""
A palindromic number reads the same both ways.
The largest palindrome made from product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# test if input is a palindrome
def is_palindrome(x):
	
	y = str(x)

	# if equals reverse then True
	if y == y[::-1]:
		return True
	else:
		return False

def largest_palindrome(lower_limit,upper_limit):
	upper = upper_limit
	lower = lower_limit
    
    # can this be intialised to int()?
	largest_pal = int()
	p_1 = int()
	p_2 = int()

    # loop numbers largest to smallest
	for i in reversed(range(lower,upper+1)):
            
		for j in reversed(range(lower,i+1)):

			current = i*j

			if current > largest_pal:

				if is_palindrome(current):
					# new largest palindrome
					largest_pal = current
					p_1 = i
					p_2 = j
					
				# else do nothing
			else:
				# else no point searching further
				break
				

			# for testing
			#print(i,j,current)

	return largest_pal, p_1, p_2

print(largest_palindrome(100,999))