# Methods --> Regular Methods, Class Method, Static Methods

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

	@classmethod
	def set_raise(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split(' - ')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('John', 'M', 70000)
emp_2 = Employee('Kate', 'K', 80000)



import datetime

my_date = datetime.date(2023,2,5)

print(Employee.is_workday(my_date))