
def logger(func):
	import logging
	logging.basicConfig(filename='demo.log', level=logging.INFO)
	def log_func(*args):
		logging.info(f"Running '{func.__name__}' with args {args}")
		print(func(*args))
	return log_func


@logger
def add(x, y):
	return x + y

@logger
def sub(x, y):
	return x - y

add(4,1)
sub(4,9)