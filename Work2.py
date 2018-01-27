import random

NUMBER_OF_EMPLOYEES = 0
EMPLOYEES_PER_DAY = 4
HOURS_IN_MONTH = 160
CURRENT_YEAR = 2018
EMPLOYEE_ID = 0
MAX_HOURS_IN_A_ROW = 24
WORKING_HOURS_PER_DAY = 8

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

DAY_NUMBERING = {
	0 : 'Monday',
	1 : 'Tuesday',
	2 : 'Wednesday',
	3 : 'Thursday',
	4 : 'Friday',
	5 : 'Saturday',
	6 : 'Sunday',
}

class Employee:
	def __init__(self, name, surname):
		global EMPLOYEE_ID
		self.id = EMPLOYEE_ID
		EMPLOYEE_ID += 1

		self.name = name
		self.surname = surname

		self.hours_in_a_row = 0
		self.workDays = []
		self.freeDays = []
		self.hours = 0

	def __repr__(self):
		return '{} {}\n'.format(
			self.name,
			self.surname
		)

class Day:
	def __init__(self, num, name):
		self.employees = []
		self.num = num
		self.name = name
		self.needed_crew = 3

	def __repr__(self):
		return '{} {}\n{}\n'.format(
			self.num + 1,
			self.name[:3],
			self.employees
		)

def check_leap_year(year):
	if year % 4 != 0: return False
	if year % 100 != 0: return True
	if year % 400 != 0: return False
	return True

def create_month(start, month):
	L30 = [3, 5, 8, 10]
	L31 = [0, 2, 4, 6, 7, 9, 11]
	if month in L30:
		month_length = 30
	elif month in L31:
		month_length = 31
	elif check_leap_year(CURRENT_YEAR):
		month_length = 29
	else:
		month_length = 28

	month_list = []

	i = 0
	for x in range(month_length):
		month_list.append(Day(x, DAY_NUMBERING[start + i]))
		i += 1
		if start + i > 6:
			i = start * (-1)

	return month_list

def fill_month_randomly(month, empl_list):
	for day in month:
		for i in range(day.needed_crew):
			empl, n = random.choice(empl_list), 0
			while empl in day.employees and n < 20:
				empl = random.choice(empl_list)
				n += 1
			day.employees.append(empl)
			empl.workDays.append(i)

def generate_month_days(month, empl_list):
	class Pointer:
		def __init__(self, empl, nxt):
			self.empl = empl
			self.next = nxt

	pnt_list = []
	for em in empl_list:
		pnt_list.append(Pointer(em, None))

	for i in range(len(pnt_list)):
		if i < len(pnt_list) - 1:
			pnt_list[i].next = pnt_list[i+1]
		else:
			pnt_list[i].next = pnt_list[0]

	curr_pnt = pnt_list[0]
	pnt_list = []

	for day in month:
		if len(empl_list) < day.needed_crew:
			print('Niewystarczajaca ilosc pracownikow... Zatrudnij kogos ziom.')
			exit()
		
		# needed_crew is full
		while len(day.employees) < day.needed_crew:
			
			# if empl in day employees list
			if curr_pnt.empl in day.employees:
				curr_pnt = curr_pnt.next
			# hours in a row
			if curr_pnt.empl.hours_in_a_row + WORKING_HOURS_PER_DAY > MAX_HOURS_IN_A_ROW:
				print('Pracownik {} wykorzystal juz dobe pracownicza ziomeczku.'.format(curr_pnt.empl))
				curr_pnt = curr_pnt.next
				break
			
			# hours in month
			if curr_pnt.empl.hours + WORKING_HOURS_PER_DAY > HOURS_IN_MONTH:
				print('Pracownik {} przekroczyl juz limit {} godzin w miesiacu. Daj mu na luz ziom.'.format(curr_pnt.empl, HOURS_IN_MONTH))
				curr_pnt = curr_pnt.next
				break

			# if everything is alright
			day.employees.append(curr_pnt.empl)
			curr_pnt.empl.hours_in_a_row += WORKING_HOURS_PER_DAY
			curr_pnt.empl.hours += WORKING_HOURS_PER_DAY
			curr_pnt.empl.workDays.append(day)
			
		for em in empl_list:
			if em not in day.employees:
				em.hours_in_a_row = 0

		print('Dodano ziomeczka {}.'.format(curr_pnt.empl))
		curr_pnt = curr_pnt.next
		# (later - different working hours, e.g. 2 work changes)
		# (later - one managing person)
		# (later - 4th sunday of employee must be free)
		# (later - 48h in a week)

def main():
	# create February, which start on Thursday 
	month = create_month(start=3, month=1)
	
	x = Employee('Andrzej', 'Wonsz')
	a = Employee('Tomasz', 'Szczadomiski')
	p = Employee('Jan', 'Stamtond')
	z = Employee('Mariusz', 'Plachta')
	w = Employee('Kwidzyniusz', 'Polaris')
	o = Employee('Kunegunda', 'Orliwierzch')
	k = Employee('Wieslawa', 'Piszczystrzal')

	employees = [x,a,p,z,w,o,k]
	#fill_month_randomly(month, employees)
	generate_month_days(month, employees)
	print(month)

	for em in employees:
		print('{}: {}'.format(em.name, len(em.workDays)))


main()




