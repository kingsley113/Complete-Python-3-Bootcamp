# some_condition = "shoes"
# something_else = "pants"

# if some_condition == "shoe":
# 	# do something
# 	print("I have shoes")
# elif something_else == "pants":
# 	# do something else
# 	print("I have pants")
# else:
# 	# do this instead of the other conditions
# 	print("I have no clothes")

# **************looping and iteration*************

iterable = [1,2,3,4,5,6,7,8,9,10]

# for item in iterable:
# 	print(item)
# 	if item % 2 == 0:
# 		print("this motha fricken number is even!")
# 	else:
# 		print("this mutha fricken number is odd!")

# sum = 0

# for num in iterable:
# 	sum += num
# 	print(sum)

# Tuple unpacking
# tup = [(1,2,3),(4,5,6),(7,8,9)]

# for a,b,c in tup:
	# print(b)

# Dictionaries:
d = {'k1': 1, 'k2': 2, 'k3': 3}

# for key in d:
# 	print(f'key: {key}')
# 	print(f'value: {d[key]}')

# or use tuple unpacking with dictionaries:
for key, value in d.items():
	print(f'key: {key}')
	print(f'value: {d[key]}')
