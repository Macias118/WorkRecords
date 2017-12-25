import calendar as clnd
import datetime
# defIne globals
NUMBER_OF_EMPLOYEES = 0
EMPLOYEES_PER_DAY = 4
HOURS_IN_MONTH = 160

'''
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
'''

class Employee:
	def __init__(self, name, surname):
		# id, name, surname 
		global NUMBER_OF_EMPLOYEES
		self.id = NUMBER_OF_EMPLOYEES
		NUMBER_OF_EMPLOYEES += 1
		self.name = name
		self.surname = surname
		self.workDays = []
		self.freeDays = []
		global HOURS_IN_MONTH
		self.hours = HOURS_IN_MONTH

	def set_free_days(self, *days_number):
		for d in days_number:
			day = Day(d)
			self.freeDays.append(d)


class Day:
	def __init__(self, num, month, year):
		self.employees = []
		self.num = num
		self.month = month
		self.year = year

	def __repr__(self):
		return '{0}.{1}.{2}'.format(self.num, self.month, self.year)


class Work:
	def __init__(self):
		self.employees = []
		self.days = []

	def __repr__(self):
		table = ''
		for employee in self.employees:
			table += '| {0}. | {1} {2} |'.format(employee.id, employee.name, employee.surname)
			table += '\n'
		return table

	def add_employee(self, *empl):
		for e in empl:
			self.employees.append(e)

	def generate_work_schedule(self, month, year):
		return [i for i in range(1, clnd.monthrange(year, month)[1]+1)]

	'''
	def generate_work_schedule(self, month, year):
		curr_year = datetime.datetime.now().year
		month_name = calendar.month_name[month]

		print("Generating schedule for...\n{0} {1}".format(month_name, curr_year))

		
		for emp in self.employees:


		print("Successful generated the schedule!")
	'''

def mainWork():
	work = Work()

	x = Employee('Andrzej', 'Wonsz')
	a = Employee('Tomasz', 'Szczadomiski')
	p = Employee('Jan', 'Stamtond')

	work.add_employee(x, a, p)

	print work.generate_work_schedule(12, 2017)

	print(work)

mainWork()

