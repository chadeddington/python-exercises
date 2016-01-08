# define a function
# : starts a code block
def sayHello():
	print "Hello World"
	# Assign variables
	name = "My name is Chad"
	print name

	name = "Now my name is Alex"
	print name

	#del name will delete the variable

# If this file was run from the command line the python interpretter will set
# __name__ equal to __main__

if __name__ == "__main__":
	sayHello()