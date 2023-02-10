def decorator_func(org_func):
	def wrapper_func(*args, **kwargs):
		
		print('Hello Universe')
		
		return org_func(*args, **kwargs)
	return wrapper_func

@decorator_func
def display():
	print('This is a display func!')
	
@decorator_func
def display_info(name, age):
	print(f"display_info ran with args ({name}, {age})")


display_info('John', 28)
