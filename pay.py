
def calculate_yearly(hourly):
	"""Calculate annual income based on a 40 hour work week """
	annual_total = hourly * 40 * 52
	return annual_total

def illinois_state_tax(income):
	"""Basic illinois flat tax"""
	return income *.0495

	## Falsified information from website
	# if income <= 2325:
	# 	return 0
	# else:
	# 	return (income - 2325) * .0495

def FICA_tax(income):
	"""FICA tax rate that return amounts based on income"""
	if income <= 137700:
		return income * .0765
	elif income > 137700 and income <= 200000:
		return ((137700 * .0765) + ((income - 133700)*.0145))
	else:
		a = 137700 * .0765
		b = (200000 - 137700) * .0145
		c = (income - 200000) * .0235
		return a + b + c

def federal_tax(income):
	"""Returns federal taxes based on progressive income.
	Brackets are based on 2020 income brackets and tax marginally """
	total_tax = 0
	inc_floor = 0
	tax_percent = [.1,.12,.22,.24,.32,.35,.37]
	tax_bracket = [9875,40125,85525,163300,207350,518400]
	
	#If income is higher than largest bracket then only the amount above said bracket is a variable
	# $156,235 is the taxed amount for all income at $518,400
	if income > 518400:
		return 156235 + (income - 518400)*.37

	#loops through the tax brackets calculating the taxes of each subset at the appropraite tax rate.
	for i in range(5):
		if income <= tax_bracket[i]:
			total_tax = total_tax + ((income - inc_floor) * tax_percent[i])
						
			break
		else:
			total_tax = total_tax + ((tax_bracket[i] - inc_floor) * tax_percent[i])
						
			inc_floor = tax_bracket[i]
	return total_tax


#data is a dictionary with key:value pairs containing the data. userinput chooses the function
def calculate_taxes(data,userinput):
	"""Pulls in dictionary with values to use and 4 inputs to choose:
	1:hourly, keywords: hourly 
	2:annual, keywords: salary
	4:tipped, keywords: hourly, hours, tips, days
	5:overtime, keywords: hourly, rate, overhours"""
	yearly = 0
	if userinput == 1:
		userIncome = float(data["hourly"])
		yearly = calculate_yearly(userIncome)

	elif userinput == 2:
		yearly = float(data["salary"])

	elif userinput == 4:
		hourly = float(data["hourly"])
		hours = float(data["hours"])
		tips = float(data["tips"])
		days = float(data["days"])
		yearly = ( days * hours * hourly * 52) + (days * tips * 52)

	elif userinput == 5:
		userIncome = float(data["hourly"])
		rate = float(data["rate"])
		hours = float(data["overhours"])
		yearly = calculate_yearly(userIncome) + (rate * hours * 52)

	taxes = federal_tax(yearly) + illinois_state_tax(yearly) + FICA_tax(yearly)

	result = yearly - taxes
	effective_tax =100 - (result / yearly)*100

	ret_string = "\nYour annual gross income: {:,.2f} \n\
Your take home income: {:,.2f}\n\
You taxes paid:{:,.2f}\n\
Your effective tax rate: {:,.3f}%\n\
Your monthly take home: {:,.2f}\n\n".format(yearly,result,taxes,effective_tax,result*.07692)
	return ret_string

#simple, less efficient method to find the correct hourly. Simple guess and check method
def calculate_required(data):
	
	userAnnual = float(data["salary"])
	x = 1
	y = 0
	while y < userAnnual:
		x= x + .01
		yearly = calculate_yearly(x)
		taxes = federal_tax(yearly) + illinois_state_tax(yearly) + FICA_tax(yearly)
		y = yearly - taxes
		

	ret_string = ("To take home ${:,.2f} annually,\n your hourly wage must be ${:,.2f}\n".format(userAnnual,x))
	return ret_string