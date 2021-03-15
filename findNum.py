import random
import itertools

print("Type 6 numbers with spaces to differentiate:")

myString = input()
print("Type the 3 digit number: ")
myTarget = int(input())

splitList = myString.split(" ")

opList = ["+","-","/","*","+0*"]

permList = list(itertools.permutations(splitList))



numList = []
for x in permList:
	i = 0
	while i <= 15625:
		nStr = str(x[0]) + opList[i%5] +str(x[1]) +opList[int((i/5)%5)] + str(x[2]) +opList[int((i/125)%5)]+ str(x[3]) + opList[int((i/625)%5)] + str(x[4]) + opList[int((i/3125)%5)] + str(x[5])
		i+=1
		T = int(eval(nStr))
		if T == myTarget:
			numList.append(nStr)
			print( nStr + " : " + str(T))



