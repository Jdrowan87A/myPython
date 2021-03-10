
def calculate_yearly(hourly):
	annual_total = hourly * 40 * 52
	return annual_total

def illinois_state_tax(income):
	if income <= 2325:
		return 0
	else:
		return (income - 2325) * .0495

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