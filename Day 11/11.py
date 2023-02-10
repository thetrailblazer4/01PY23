#Inheritance/ Subclasses

class Employee:

	raise_amount = 1.05
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def full_name(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
	raise_amount = 1.09

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, last, pay, emps = None):
		super().__init__(first,last,pay)

		if emps is None:
			self.emps = []
		else:
			self.emps = emps


	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)


	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)


	def get_emps(self):
		for emp in self.emps:
			print(emp.full_name())

emp_1 = Employee('John', 'M', 70000)
emp_2 = Developer('Kate', 'K', 70000, 'Python')	
mgr_1 = Manager('Tom', 'H', 90000, [emp_1])	

# mgr_1.get_emps()

mgr_1.add_emp(emp_2)
mgr_1.remove_emp(emp_1)
mgr_1.get_emps()

# print(help(Developer))

print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))

print(issubclass(Manager, Employee))