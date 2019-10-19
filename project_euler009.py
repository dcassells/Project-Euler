"""
Q.
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

-------------
Approach:
a and b fixes c so we can use these to loop, rather than looping all three.

-------------
Use:
python project_euler009.py
"""

n = 1000

triplet_found = False

for a in range(1,int(n/3)+1):

	for b in range(a+1,int(n/2)+1):

		c = n - a - b

		if (a*a + b*b == c*c):
			triplet_found = True
			print('Triplet found\n----------')
			print('a =',a,'\nb =',b,'\nc =',c)
			print('Product is',a*b*c)

			break

	if triplet_found:
		break

if not triplet_found:
	print('No triplet found')