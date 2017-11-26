# defIne globals
NUMBER_OF_EMPLOYEES = 0
EMPLOYEES_PER_DAY = 4

class Calendar:
	def __init__(self):
		self.numberOfDays = 30
		self.days = []


class Employee:
	def __init__(self, n, s):
		# id, name, surname 
		global NUMBER_OF_EMPLOYEES
		self.id = NUMBER_OF_EMPLOYEES
		NUMBER_OF_EMPLOYEES += 1
		self.name = n
		self.surname = s
		self.workDays = []
		self.freeDays = []


class Day:
	def __init__(self):
		self.employees = []


class Work:
	def __init__(self):
		self.employees = []

	def __repr__(self):
		table = ''
		for employee in self.employees:
			table += '| {0}. | {1} {2} |'.format(employee.id, employee.name, employee.surname)
			table += '\n'
		return table

	def add_employee(self, *empl):
		for e in empl:
			self.employees.append(e)


def mainWork():
	work = Work()

	x = Employee('x', 'y')
	a = Employee('a', 'b')
	p = Employee('p', 'r')

	work.add_employee(x, a, p)

	print(work)

mainWork()

