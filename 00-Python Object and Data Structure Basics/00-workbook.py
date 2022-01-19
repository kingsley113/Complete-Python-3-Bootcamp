# print("hello world!")
# print("goodbye world!")

# STRINGS**********************************************************************
# myString = "Death Stranding is fun"
# # print(myString[3]) #strings are indexed
# # print(myString[-3])

# # slicing
# print(myString[2:]) #grab index 2 to the end of string 
# print(myString[:3]) #grab from beginning to just before index 
# print(myString[4:8]) #grab from index 4 to 7
# print(myString[2:8:2]) #grab from index 2 to 4 with step size of 2

# # string properties and methods
# lastWord = myString[-3:]
# print("Games are " + lastWord)
# print( 'z' * 10)

# x = 'Hello World'
# print(x.upper())
# print(x.split())

# # string formatting
# game = 'Cyberpunk 2077'
# rating = 'glitchy'
# print('{} is a really {} game.'.format(game, rating)) # .format() methods
# print('{1} is a really {0} game.'.format('Beautiful', 'Red Dead Redemption'))
# print('{g} is a really {r} game.'.format(r='Beautiful', g='Red Dead Redemption'))

# result = 100/777
# print('The result was {r:1.4f}'.format(r=result)) # precision and width modifier r:width.precision f

# print(f'Hello, my favorite game is {game}')

# LISTS************************************************************************
# Lists are similar to arrays in other languages
# myList = [1,2,3,4,5]
# print(myList)
# print(len(myList))
# print(myList[:3]) # slicing works the same as strings
# anotherList = [6,7,8]
# print(myList + anotherList)
# newList = myList + anotherList
# print(newList)

# myList[0] = 'Hippo'
# print(myList)
# myList.append('Hungry') # append() is same as push() in js/ruby
# print(myList)
# lastElement = myList.pop() # pop() removes and returns the last element of list
# print(lastElement, myList)
# anElement = myList.pop(1) # can specify an index to pop and return
# print(anElement)
# # sort
# newList = [62,83,39,54,9,14,0,25,145]
# print(newList)
# newList.sort()
# print(newList)
# newList.reverse()
# print(newList)

# DISCTIONARIES****************************************************************
# dicts are similar to hashes in ruby or objects in js
# myDict = {'key1': 'value1', 'key2':'value2'}
# print(myDict['key1'])
# # keys need to be strings
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())

# TUPLES***********************************************************************
# similar to lists but immutable, made with () instead of []
# t = (1,2,3)
# myList = [1,2,3]
# print(len(t)) 
# tup = ('1','2','3','3')
# print(tup.count('3'))
# print(tup.index('2'))

# SETS*************************************************************************
# sets only accept unique values
# myList = [1,2,2,3,3,4,4,5,5,6,7,8,9,9,9,0]
# print(set(myList))


# BOOLEAN**********************************************************************
# True
# False # capitalize True/False

# FILE READ/WRITE**************************************************************
# myFile = open('./00-Python Object and Data Structure Basics/test.txt')
# contents = myFile.read()
# print(contents)


with open('./00-Python Object and Data Structure Basics/test.txt', mode='a') as newFile:
	newFile.write('\nThird Line')

with open('./00-Python Object and Data Structure Basics/test.txt', mode='r') as newFile:
	contents = newFile.read()

print(contents)

# print(contents)
with open('./00-Python Object and Data Structure Basics/test.txt', mode='w') as reset:
	reset.write('First Line\nSecond Line')

with open('./00-Python Object and Data Structure Basics/test.txt', mode='r') as newFile:
	contents = newFile.read()
	# modes: r = read, w = write (overwrite), a = append, r+ = reading and writing, w+ = overwrite or create new file

print(contents)