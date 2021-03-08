import random
import shutil
import psutil
import H
import os

print("Choose which sections to print: ")

section = int(input())

#loops and strings
if section == 1 or section ==10:
	x = 0
	while x <= 5:
		print(x)
		x += 1

#basic string functions and a function
myString = "This is a basic string to show what can happen 1324"
newString = myString.split()
if section == 2 or section == 10:
	print(newString)
newString2 = " ".join(newString)
if section == 2 or section == 10:
	print(newString2)


def myFunction(string, x):
	retString = ""
	for letter in myString:
		if x == 1:
			if letter.isalpha():
				retString = retString + letter.upper()
		elif x ==0:
			if letter.isnumeric():
				retString = retString + letter
		else:
			retString = "Nothing at all"
	return retString


if section == 2 or section == 10:
	print(myFunction(myString,1))
	print(myFunction(myString,0))



#Formating numbers
myNumList = [12.32,3.543,3234.2,43,43,43.121,12312.3,105.34]
if section == 3 or section == 10:
	print("\nNormal")
	for x in myNumList:
		print(x)

	print("\n{:.2f}")
	for x in myNumList:
		print("{:.2f}".format(x))

	print("\n{:>8.3f}")
	for x in myNumList:
		print("{:>8.3f}".format(x))

#basics on dictionaries

myDict = {"alpha":"AlphaStored","beta":4,"gamma":[1,2,3,4],"delta":"myDelta"}
if section == 4 or section == 10:
	print(myDict["alpha"])

# counts letters in the string
newDict={}
for letter in myString:
	if letter.isalpha():
		if letter.upper() not in newDict:
			newDict[letter.upper()] = 0
		newDict[letter.upper()] += 1

#raw dictionary print
if section == 4 or section == 10:
	print(newDict)

#prints the key and value in no certain order
if section == 4 or section == 10:
	for a,b in newDict.items():
		print(a,b)

	print("\n")
	#prints in order of the key
	for a,b in sorted(newDict.items()):
		print(a,b)

##utils
if section == 5 or section == 10:
	du = shutil.disk_usage("/")
	print(du)
	x = psutil.cpu_percent(0.1)
	print(x)
	H.run_Check()

if section == 6 or section ==10:
	#if a file is opened with "w", the file content will be erased at open.
	f = open("myText.txt","a")
	inp = input()
	
	if inp == "x":
		f.close()
		f = open("myText.txt","w")
		f.close()
	else:
		f.write(inp + "\n")
		f.close()

	with open("myText.txt") as file:
		index = 1
		for line in file:
			print(str(index) +": "+ line.strip())
			index += 1
	
	#os module
	if os.path.exists("othertext.txt"):
		os.remove("othertext.txt")

	ff = open("thisText.txt","a")
	ff.write("This is a line\n")
	ff.close()

	os.rename("thisText.txt", "othertext.txt")

	ff = open("othertext.txt")
	print(ff.readline())
	ff.close()

