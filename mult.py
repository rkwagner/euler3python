#------------------------
#Author:	Ryan Wagner
#Date:		September 3, 2014
#Description:	Finds the largest prime factor of a large number.
#Input:		Number to check.
#Output:	Largest prime number.
#------------------------
#Strategy:	Reduce possibilities to the square root of the total.
#		Reduce again to the square root of the first square,
#		To check for primality in the range.
#------------------------
from math import sqrt
num = 600851475143
for i in range(2, int(sqrt(num))+1):
	if num % i == 0:
		k = num/i
		x=0
		for j in range(2, int(sqrt(i))+1):
			if i % j == 0:
				x=x+1
		if x == 0:
			print i
		x=0
		for j in range(2, int(sqrt(k))+1):
			if k % j == 0:
				x=x+1
		if x == 0:
			print k
		x=0
