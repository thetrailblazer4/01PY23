class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def full_name(self):
		return f"{self.first} {self.last}"


emp_1 = Employee('John', 'M', 70000)
emp_2 = Employee('Kate', 'K', 80000)

# print(emp_1.first)
# print(emp_2.first)

# print(f"{emp_1.first} {emp_1.last}")
# print(f"{emp_2.first} {emp_2.last}")

print(emp_1.full_name())
print(emp_2.full_name())
