# defIne globals
NUMBER_OF_EMPLOYEES = 0
EMPLOYEES_PER_DAY = 4
HOURS_IN_MONTH = 160

class Calendar:
	weekDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	def __init__(self):
		self.freeDays = []
		self.numberOfDays = 30
		self.days = []
		weekDayPointer = 2
		for i in range(self.numberOfDays):
			self.days.append(Day(self.weekDays[weekDayPointer], i + 1))
			weekDayPointer += 1
			if weekDayPointer > len(self.weekDays) - 1:
				weekDayPointer = 0


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
		global HOURS_IN_MONTH
		self.hours = HOURS_IN_MONTH


class Day:
	def __init__(self, name, num):
		self.employees = []
		self.name = name
		self.num = num

	def __repr__(self):
		return '{0}. {1}'.format(self.num, self.name)


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

	def create_calendar(self):
		self.calendar = Calendar()
		for day in self.calendar.days:
			print('{}'.format(day))


def mainWork():
	work = Work()

	x = Employee('x', 'y')
	a = Employee('a', 'b')
	p = Employee('p', 'r')

	work.add_employee(x, a, p)

	work.create_calendar()

	print(work)

mainWork()

