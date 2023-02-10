def find_index(args_lst, target):
	for index, value in enumerate(args_lst):
		if value == target:
			return index
	return -1

new_var = 'Hello world!'