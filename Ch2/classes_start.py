class myClass():
	def method1(self):
		print "myClass method1"
	def method2(self):
		print "The second class"

# If a class inhertis another class, you pass the parent class as
# a parameter the child class
class anotherClass(myClass):
	def method1(self):
		print "another class method1"
      
def main():
  testClass = myClass()
  testClass.method1()
  class2 = anotherClass()
  class2.method1()
  class2.method2()


if __name__ == "__main__":
  main()
