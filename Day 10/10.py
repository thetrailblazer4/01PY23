# Class Variable

class Employee:

	raise_amount = 1.05
	num_of_emps = 0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay
		
		Employee.num_of_emps += 1

	def full_name(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('John', 'M', 70000)
emp_2 = Employee('Kate', 'K', 80000)

emp_1.raise_amount = 1.07

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)