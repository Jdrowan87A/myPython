import random

# nested for loop with formating. Note that integers won't print into a string - 
# unless you changed the type to str(). If you are just printing a number, then no -
# to change
for x in range(5):
    for y in range(x):
    	r = random.randrange(0,100000) / 1000
    	s = " Random: {:>6.3f}".format(r) 
    	print("x:" + str(x) +" y:" + str(y) + s)

#format on the end of a string allows us to add variables into the string at locations
name = "Joshua"
fString = "Hello {}, and welcome".format(name) 
print (fString)
print (fString[:4])
print (fString[1:3])

#lists are the basic arrays of Python. You can add multi dimensional directly in.
#iterating over the list uses a simple or loop without indexing.
myList = ['first','second',['third', 'fourth'], 6, 9]
for x in myList:
	print(x)

# this is a basic function that takes an integer and returns 4 items in a tuple
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

#enumerate adds numbers to the start, 
mySpanish = ['uno','dos','tres','quatro']
for index, num in enumerate(mySpanish):
	print("{} - {}".format(index + 1, num))

## quiz question
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


## dictionaries use keys and values
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group,users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			user_groups[user] = user_groups.get(user,[]) +[group]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#############################

## writing a class

class MyClass:
	def __init__(self, name, size):
		self.name = name
		self.size = size

	def sparkle(self):
		"""Reduces size by 5 and prints new size. This is DOCSTRING """
		self.size -= 5
		print(self.size)

	def __str__(self):
		return "Stop printing my Shit!!!"

Josh = MyClass("Joshua", 160)


print(Josh.size)
Josh.sparkle()
print(Josh)
