import random


for x in range(5):
    for y in range(x):
    	r = random.randrange(0,100000) / 1000
    	s = " Random: {:>6.3f}".format(r) 
    	print("x:" + str(x) +" y:" + str(y) + s)
name = "Joshua"
fString = "Hello {}, and welcome".format(name) 
print (fString)
print (fString[:4])

myList = ['first','second',['third', 'fourth'], 6, 9]
for x in myList:
	print(x)

def myPowers(x):
	squared = x**2
	cubed = x**3
	quad = x**4
	pent = x**5
	return squared,cubed,quad,pent

results = myPowers(3)
print(results)
print(results[2])
a,b,c,d = myPowers(4)
print(a,b,c,d)

mySpanish = ['uno','dos','tres','quatro']
for index, num in enumerate(mySpanish):
	print("{} - {}".format(index + 1, num))