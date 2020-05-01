# Author: Jossie Calderon

'''R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def is_multiple(n, m):
	if m % n == 0:
		return True
	else
		return False

'''R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def even(k):
	bool isEven = True:
	count = 0
	while count != k: # if k == 0, the loop won't run.
		isEven = !isEven
		count += 1
	return isEven

'''R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''

def minimax(data):
	min = data[0]
	max = data[0]
	for elem in data:
		if elem < min:
			min = elem
		if max < elem:
			max = elem
	return (min, max)

'''R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def sumSquares(n):
	sum = 0
	for i in range(n):
		sum += i*i
	return sum

'''R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
'''

def sumSquaresLC(n):
	return sum([i*i for i in range(1, n)])

'''R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
def sumSquaresOdd(n):
	sum = 0
	for i in range(1, n, 2):
		sum += i*i
	return i

'''R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
'''

def sumSquaresOddLC(n):
	return sum([i*i for i in range(1, n, 2)])

'''R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
'''

# n + k


'''R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
'''

# range(50, 90, 10)

'''R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
'''

# range(8, -10, -2)

'''R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
'''

[2**i for i in range(9)]


'''R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
'''

def randomChoice(someList):
	return someList[randrange(len(someList))]
