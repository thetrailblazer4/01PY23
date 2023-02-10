# # Decorators <-- Closures <-- First Class Functions

# '''
# First-class Function
# A programming language is said to have First-class functions 
# when functions in that language are treated like any other variable. 

# For example, in such a language, 
# a function can be passed as an argument to other functions, 
# can be returned by another function and 
# can be assigned as a value to a variable.

# '''

# def square(x):
# 	return x * x

# print(square(2))
# result = square
# print(result(6))

# def outer_func(msg):
# 	def inner_func():
# 		print(msg)
# 	return inner_func

# result = outer_func('Hi')
# result()

# define a func which take a list as an argument and returns list of sqares of nums

# [1,2,3,4] --> [1,4,9,16] 

# def square(x):
# 	return x * x

# def cube(x):
# 	return x * x * x


# def my_func(func, args_lst):
# 	result = []
# 	for i in args_lst:
# 		result.append(func(i))
# 	return result

# print(my_func(square, [1,2,3,4]))
# print(my_func(cube, [1,2,3,4]))


def decorator_func(org_func):
	def wrapper_func():
		print('hello universe!')
		return org_func()
	return wrapper_func

@decorator_func
def display():
	print('This is a display func!')
	
@decorator_func
def demo_display():
	print('demo_display func!')

# dec_disp = decorator_func(display)
# dec_disp()

display()

demo_display()
