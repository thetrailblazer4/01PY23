class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{self.first}.{self.last}@company.com'
		
	@property
	def email(self):
		return f'{self.first}.{self.last}@company.com'

	@property
	def full_name(self):
		return f"{self.first} {self.last}"


emp_1 = Employee('John', 'M', 70000)

emp_1.first = 'Tom'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)
print(emp_1.email)
