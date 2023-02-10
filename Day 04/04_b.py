# def hello_func(greeting, name ='You'):
# 	return f"{greeting} {name}"


# print(hello_func('Hello'))


def emp_info(*args, **kwargs):
	print(args)
	print(kwargs)

emp_info('Python', 'Java', name='John')

# import builtins

# print(dir(builtins))

# num_1 = [1,2,3]
# print(help(num_1))