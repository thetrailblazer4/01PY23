'''
Functions
	Importance
	How to create

	DRY --> Don't Repeat Yourself
'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)


def square(length, angle):
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)

for i in range(100):
	square(100, 90)
	my_turtle.right(11)


# list_1 = [1,2,3,4,5,7,8]
# print(list(range(10)))


# for i in range(100):
# 	print('hello')




turtle.done()