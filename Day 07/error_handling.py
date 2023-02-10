
# FileNotFoundError
# NameError



try:
	f = open('demos.txt')
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
finally:
	print('Executing.....')
