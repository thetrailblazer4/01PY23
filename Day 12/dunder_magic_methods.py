class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def full_name(self):
		return f"{self.first} {self.last}"

	def __repr__(self):
		return f"Employee('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.full_name()} - {self.email}"

emp_1 = Employee('John', 'M', 70000)
emp_2 = Employee('Kate', 'K', 80000)

# print(emp_1.first)
# print(emp_1.full_name())
print(emp_1)
# __repr__
# __str__

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())