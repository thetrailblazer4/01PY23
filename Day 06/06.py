# Variables --> Locally --> Enclosing --> Global --> Builtins (LEGB)

# x = 'global x'


# def demo(args):
# 	x = 'local x'
# 	print(args)


# demo('local z')
# print(args)

# def min():
# 	pass

# nums_1 = [45,56,12,69,24]

# result = min(nums_1)
# print(result)


# import builtins

# # print(dir(builtins))

# x = 'global x'

# def outer():
# 	x = 'outer x'

# 	def inner():
# 		x = 'inner x'
# 		print(x)

# 	inner()
# 	print(x)


# outer()