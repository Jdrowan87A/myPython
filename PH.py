
def calculate_yearly(hourly):
	annual_total = hourly * 40 * 52
	return annual_total

def illinois_state_tax(income):
	return income *.0495

	## Falsified information from website
	# if income <= 2325:
	# 	return 0
	# else:
	# 	return (income - 2325) * .0495

def FICA_tax(income):
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
	total_tax = 0
	inc_floor = 0
	tax_percent = [.1,.12,.22,.24,.32,.35,.37]
	tax_bracket = [9875,40125,85525,163300,207350,518400]
	
	if income > 518400:
		return 156235 + (income - 518400)*.37

	for i in range(5):
		if income <= tax_bracket[i]:
			total_tax = total_tax + ((income - inc_floor) * tax_percent[i])
						#print("TEST:"+str(total_tax),str(inc_floor),str(tax_percent[i]))
			break
		else:
			total_tax = total_tax + ((tax_bracket[i] - inc_floor) * tax_percent[i])
						#print("TEST2:"+str(total_tax),str(inc_floor),str(tax_percent[i]))
			inc_floor = tax_bracket[i]
	return total_tax



def calculate_taxes(userinput):
	yearly = 0
	if userinput == 1:
		print("What is you hourly wage? (no dollar signs):", end="")
		userIncome = float(input())
		yearly = calculate_yearly(userIncome)

	elif userinput == 2:
		print("What is your annual salary? (no dollar signs):", end="")
		yearly = float(input())

	elif userinput == 5:
		print("Hourly Wage: ",end="")
		hourly = float(input())
		print("Average Hours per Day: ",end="")
		hours = float(input())
		print("Average Tips per Day: ",end="")
		tips = float(input())
		print("Average Days per Week: ",end="")
		days = float(input())
		yearly = ( days * hours * hourly * 52) + (days * tips * 52)

	elif userinput == 4:
		print("What is you hourly wage? (no dollar signs):", end="")
		userIncome = float(input())
		print("What is your overtime rate? (1.5 is time and a half)", end="")
		rate = float(input())
		print("Average overtime hours per week?: ",end="")
		hours = float(input())
		yearly = calculate_yearly(userIncome) + (rate * hours * 52)

	taxes = federal_tax(yearly) + illinois_state_tax(yearly) + FICA_tax(yearly)

	result = yearly - taxes
	effective_tax =100 - (result / yearly)*100

	print("\nYour annual gross income: {:,.2f} \n\
Your take home income: {:,.2f}\n\
You taxes paid:{:,.2f}\n\
Your effective tax rate: {:,.3f}%\n\
Your monthly take home: {:,.2f}\n\n".
	format(yearly,result,taxes,effective_tax,result*.07692))

def calculate_required():
	print("Desired take home: ",end="")
	userAnnual = float(input())
	x = 1
	y = 0
	while y < userAnnual:
		x= x + .01
		yearly = calculate_yearly(x)
		taxes = federal_tax(yearly) + illinois_state_tax(yearly) + FICA_tax(yearly)
		y = yearly - taxes
		

	print("To take home ${:,.2f} annually, your hourly wage must be ${:,.2f}\n".format(userAnnual,x))