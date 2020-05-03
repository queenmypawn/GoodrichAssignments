'''C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''

def reverseIntegers(listOfInts):
	# equivalent: return list(reversed(listOfInts))
	# without using reversed(iterable):
	# Pseudo-code:
	# create a list
	# do a reversed for loop
	# append the integers to the new list using the index.

	reversedInts = []
	for i in range(len(listOfInts) - 1, 0, -1):
		reversedInts.append(listOfInts[i])
	return reversedInts

'''C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''

def isThereOddProduct(listOfInts):
	# An odd number is only the product of two odd numbers
	bool oddProd = False
	count = 0
	for elem in list:
		if !isEven(list[elem]): # requires 'import 1_reinforcement.py'
			count += 1
		if count == 2:
			return True
	return False

'''C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''

# Create a set
# If the set elements do not have the same counts as the list,
# elements are repeated
def numbersAreAllDifferent(listOfNums):
	if len(set(listOfNums)) == len(listOfNums):
		return True
	return False


'''C-1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j]= factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
'''

# The contents of the list may be immutable, but the references aren't. The scale function
# only changes the references.

'''C-1.17 Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val= factor
Explain why or why not.
'''

# This is a different way to iterate through the list, so the program will run.
# However, it doesn't return the same output. It sets all of the elements equal
# to the factor. Therefore, no, it doesn't run properly.

'''C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''

# The trick is to realize every element in the list is a factor of 2,
# hence the list boils down to [0, 1, 3, 6, 10, ..., 45] and every element
# is multiplied by 2 at the end. The essential rule is then

# [sum(range(i+1))*2 for i in range(10)]

'''C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a ,b ,c , ...,z ], but without having to type all 26 such
characters literally.
'''

# [chr(int(f"{i}")) for i in range(97, 123)]

'''C-1.20 Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
'''

# Fisher-Yates is more efficient, but this works too
def myShuffle(data): # requires 'from random import randint'
	shuffledList = []
	while len(shuffledList) != len(data):
		randomObj = data[randint(0, len(data) - 1)]
		if randomObj not in shuffledList or data.count(randomObj) != shuffledList.count(randomObj):
			shuffledList.append(randomObj)
	return shuffledList


'''C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
'''
def readLinesFromInput():
lines = []
reverseLines = []
while True:
	try:
		lines.append(input())
	except EOFError:
		for i in range(len(lines) - 1, -1, -1):
			print(lines[i])

'''C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.
'''

def dotProduct(listA, listB):
	if len(listA) != len(listB):
		return [0]
	else: # Strictly speaking, the dot product is a scalar, so it should return
			# the sum instead.
		return [listA[i]*listB[i] for i in range(len(listA))]


'''C-1.23 Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
'''
def copyList(originalList):
	try:
		for i in range(n):
			myList.append(originalList[i])
	except IndexError:
		print("Don’t try buffer overflow attacks in Python!")


'''C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
'''

def vowelCounter(myStr):
	vowels = [a, e, i, o, u]
	count = 0
	for elem in str:
		if elem in vowels:
			count += 1
	return count


'''C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
'''

def removePunct(myStr):
	newStr = ''
	for elem in myStr:
		if elem.isalpha() || ' ':
			newStr += elem
	return newStr

'''C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
'''

# Strictly speaking, the authors probably meant 'a - b = c' (in the second conditional).
def correctFormula(a, b, c):
	if a + b == c:
		return f'{a} + {b} = {c}'
	elif b - c == a:
		return f'{a} = {b} - {c}'
	elif a * b == c:
		return f'{a} * {b} = {c}'
	else:
		return 'Not Compatible'

'''C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages.
'''

def factors(n): # generator that computes factors
	k = 1
	while k*k < n: # while k < sqrt(n)
		if n % k == 0:
			yield k
		k += 1
	if k*k == n:  # special case if n is perfect square
		yield k
	k -= 1 # to not re-iterate this same number.
	while k != 0: # decrease by 1 to report the factors in order.			
		if n % k == 0:
			yield n // k
		k -= 1


'''C-1.28 The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is de-
fined as

normV = (v_1**p + v_2**p + ... + v_n**p)**(1/p)

For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Eu-
clidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of (4**2 + 3**2)**(1/2) = 5. Give an implementation of a 
function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
'''

def norm(v, p = 2):
	# v is the list of co-ordinates
	# p is the number used for the exponent.
	return sum([v[i]**p for i in range(len(v))])
