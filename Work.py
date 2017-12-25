import calendar as clnd
import datetime
from random import randint

#
# define globals
#
NUMBER_OF_EMPLOYEES = 0
EMPLOYEES_PER_DAY = 4
HOURS_IN_MONTH = 160

MONTH_NUMBERING = {
	0 : "January",
	1 : "February",
	2 : "March",
	3 : "April",
	4 : "May",
	5 : "June", 
	6 : "July",
	7 : "August",
	8 : "September",
	9 : "October",
	10 : "November", 
	11 : "December"
}

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
		self.schedule = {}

	def __repr__(self):
		table = ''
		print('ID\tName\tSurname\t  Number of days')
		for employee in self.employees:
			table += '| {0}. | {1} {2} | {3} |'.format(employee.id, employee.name, employee.surname, len(employee.workDays))
			table += '\n'
		return table

	def add_employee(self, *empl):
		for e in empl:
			self.employees.append(e)

	def generate_work_schedule(self, month, year):
		self.days = [i for i in range(1, clnd.monthrange(year, month)[1]+1)]
		for day in self.days:
			num_empl = randint(0, len(self.employees)-1)
			self.employees[num_empl].workDays.append(day)
			self.schedule[day] = "{0} {1}".format(self.employees[num_empl].name, self.employees[num_empl].surname)

		return self.schedule

	def assign_day_to_employee(self, empl, day):
		empl.workDays.append(day)

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

	current_month = 11

	work.add_employee(x, a, p)

	print MONTH_NUMBERING[current_month]
	schedule = work.generate_work_schedule(current_month, 2017)
	print("\n".join("{}: {}".format(k, v) for k, v in schedule.items()))
	print(work)

mainWork()

