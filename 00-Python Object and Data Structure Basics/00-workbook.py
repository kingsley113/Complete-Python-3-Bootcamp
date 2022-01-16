# print("hello world!")
# print("goodbye world!")

# STRINGS**********************************************************************
myString = "Death Stranding is fun"
# print(myString[3]) #strings are indexed
# print(myString[-3])

# slicing
print(myString[2:]) #grab index 2 to the end of string 
print(myString[:3]) #grab from beginning to just before index 
print(myString[4:8]) #grab from index 4 to 7
print(myString[2:8:2]) #grab from index 2 to 4 with step size of 2

# string properties and methods
lastWord = myString[-3:]
print("Games are " + lastWord)
print( 'z' * 10)

x = 'Hello World'
print(x.upper())
print(x.split())

# string formatting
game = 'Cyberpunk 2077'
rating = 'glitchy'
print('{} is a really {} game.'.format(game, rating)) # .format() methods
print('{1} is a really {0} game.'.format('Beautiful', 'Red Dead Redemption'))
print('{g} is a really {r} game.'.format(r='Beautiful', g='Red Dead Redemption'))

result = 100/777
print('The result was {r:1.4f}'.format(r=result)) # precision and width modifier r:width.precision f

print(f'Hello, my favorite game is {game}')

# LISTS************************************************************************