'''
Data Structure - 
a data organization, management, and storage format that is usually 
chosen for efficient access to data.
'''
# [item1, item2, item3]
# message = ['Hello', 'Hi', 'Bye']



# for index, item in enumerate(message):
# 	print(f"{index} - {item}")



# in

# print('Hi' in message)
# print(message)


# new_msg = ['Hey', 'Goodbye']

# message.append(new_msg)
# message.insert(0, 'Hey')
# message.extend(new_msg)

# message.remove('Hi')
# message.pop(1)

# print(message)


# message = 'Hello - Hi - Bye'

# #from str to list
# new_list = message.split(' - ')
# print(type(new_list))

# #from list to str
# new_str = ' | '.join(new_list)

# print(type(new_str))


# # Mutable

# list_1 = ['Hello', 'Hi', 'Bye']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Hey'

# print(list_1)
# print(list_2)


# # Immutable -> Tuple
# tuple_1 = ('Hello', 'Hi', 'Bye')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Hey'

# print(tuple_1)
# print(tuple_2)

#Sets --> used for membership test
# messages = {'Hello', 'Hi', 'Bye', 'Hello', 'Hi','Hello'}
# msg = {'Hello', 'Hey', 'Bye'}

# print(msg.intersection(messages))
# print(msg.difference(messages))
# print(msg.union(messages))


# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty sets
# empty_set = {}  #<- This is also used for creating dict
# empty_set = set()
