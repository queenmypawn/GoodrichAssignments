'''P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
'''

# itertools.permutations can be used, but that would defeat the purpose
# of the exercise

# 1) Create a generator
# 2) Call the generator with the string as the parameter.

# No further assumptions are made. This function, therefore, has not been
# generalized for all strings, but could be done.

# Initialize myStr = 'catdog',
# then call the below function
def allStrings(myStr):
	count = 0



'''P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''

# We can do this by examining the bits:
def divideThisManyTimes(num):
	myBit = f'{num:08b}'
	if myBit[0] == 1 && myBit.count('1') == 1:
		return 'infinity times.' # The number is an exponent of 2, so you'll never get
		# a value less than 2.
	if num < 2:
		return '0 times.' # It's already less than 2.
	else:
		count = 0
		while num > 2:
			num = num / 2
			count += 1
		return f'{count} times.'



'''P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
'''
def returnChange(chargedAmt, givenAmt):
	change = givenAmt - chargedAmt




'''P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
'''




'''P-1.33 Write a Python program that simulates a handheld calculator. Your pro-
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each op-
eration is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
'''




'''P-1.34 A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
'''

# 'from random import randrange' required
def punishmentStr():
	pStr = 'I will never spam my friends again.'
	length = len(pStr)
	sentenceNumberTypoIndexes = set()
	characterNumberTypoIndexes = set()
	while len(sentenceNumberTypoIndexes) != 8:
		sentenceNumberTypoIndexes.add(randrange(100))
	while len(characterNumberTypoIndexes) != 8:
		characterNumberTypoIndexes.add(randrange(length))
	count = 0

	# Turn the sets back to lists to make them subscriptable
	sentenceNumberTypoIndexes = list(sentenceNumberTypoIndexes)
	characterNumberTypoIndexes = list(characterNumberTypoIndexes)
	for i in range(100):
		if i in sentenceNumberTypoIndexes:
			letterToBeReplacedIndex = characterNumberTypoIndexes[count]
			randomTypo = chr(randrange(97, 124))
			while randomTypo == pStr[letterToBeReplacedIndex]:
				randomTypo = chr(randrange(97, 124))
			typoStr = pStr[:letterToBeReplacedIndex] + randomTypo + pStr[letterToBeReplacedIndex + 1:]
			pStr = typoStr
			count += 1
		print(f'{i + 1}. {pStr}')
		pStr = 'I will never spam my friends again.'

'''P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,... ,100.
'''

# Requires 'from random import randrange'
# Assuming non-leap years
def birthdayParadox():
	numOfBDays = [i for i in range (5, 101, 5)]
	for j in numOfBDays:
		bDayList = [randrange(365) for i in range(j)]
		# print(f'{j} days contains {bDayList}') # Include this to see the exact dates. (Messy!)
		lenBDaySet = len(set(bDayList))
		lenBDay = len(bDayList)
		sameBDays = lenBDay - lenBDaySet
		if sameBDays != 0:
			print(f"For n = {j}, {sameBDays} birthdays were the same!")
		# Below prints the probabilities.
		'''complementProbabilities = [(365 - i)/365 for i in range(j)]
		product = 1
		for i in complementProbabilities:
			product *= i
		probabilityOfSameBDay = 1 - product
		print(f'{j} is {probabilityOfSameBDay}')'''


'''P-1.36 Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
'''

# 1) collect input:
# myInput = input()

# 2) create the function:
def countReps(myStr):
	words = myStr.split(' ')

	# create a set to avoid repetition.
	setOfWords = set(words)

	for word in setOfWords:
		count = words.count(word)
		print (f'{word} appears {count} times.')
