# Textual Data --> (Strings) '', " ", ''' ''', """ """

# Executes one line at a time

# message = """John's world
# Hello Universe"""

# print(message)

message = 'Hello'
name = 'John'

# greeting = message + ','+ ' ' + name

greeting = '{}, {}! {}'.format(message, name, message)
greeting = f'{message}, {name}!'

'''
Number 
Whole Number --> integers
decimals --> floats

Arithmetic Operators
+
-
*
/
//
**
%

'''
# #Comparisons:
# 	==
# 	!=
# 	>
# 	<
# 	>=
# 	<=

# num = 1.4

# print(type(num))

# num_1 = 3
# num_2 = 2

# result = num_1 + num_2
# print('The sum of {} and {} is {}'.format(num_1, num_2, result))
# print(f'The sum of {num_1} and {num_2} is {result}')


# num = 1

# # num = num + 1
# num += 1

# print(num)

num_1 = '100'
num_2 = 200

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)