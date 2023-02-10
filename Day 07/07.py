# f = open('demo.txt')

# print(f.read())

# print(f.closed)
# f.close()
# print(f.closed)


# with open('new_demo.txt', 'w') as f:
# 	f.write('Hello World!')
# 	f.seek(0)
# 	f.write('hey')


with open('demo.txt', 'r') as rf:
	with open('demo_copy.txt', 'w') as wf:
		for line in rf:
			wf.write