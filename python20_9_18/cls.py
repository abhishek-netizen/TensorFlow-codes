'''class Employee:
	h=40
# create object 	
e1=Employee()
e2=Employee()
print(e1.h)
print(e2.h)	

e1.name='sam'
e2.name='john'
print(e1.name)
print(e2.name)'''
'''
# self parameter 
class Employee:
	def empDetails(self):
		print('Hello')
	def printDetails(self):
		print('Hello Python')
emp1=Employee()
emp1.empDetails()
Employee.empDetails(emp1)
emp1.printDetails()		
# instance attribute inside the class
class Employee:
	def empDetails(self):
		#instance attribute 
		self.name='sam' # instance attribute 
		age=25 # we cant use this attribute outside this funcion
		print(self.name)
		print(age)
	def printDetails(self):
		print(self.name)
		#print(age) # wrong
# create object 
emp1=Employee()
emp1.empDetails()
emp1.printDetails()	'''	

# __init__() --> special function 
# initialize the variable 
'''class Employee:
	def enterDetails(self):
		self.name='sam'
	def printDetails(self)
		print(self.name)
emp1=Employee()
##emp1.enterDetails()
emp1.printDetails()

the object was unable to find the instance attribute self.name 
because we called the second method before the first method
the initialization happen in first method
now we need a function in which we can initialize all the attribute or our class before they are being used.
now python helps us to do that by making use of a special method __int__()
which is the first method that is called at the time of object creation

'''
'''
class Employee:
	def __init__(self):
		self.name='san'
	def printdetails(self):
		print(self.name)
emp1=Employee()
##emp1.enterDetails()
emp1.printdetails()		'''

	
class Employee:
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	def fullName(self):
		return '{} {}'.format(self.fname,self.lname)
'''		
emp1=Employee('sam','kumar',1000)
emp2=Employee('john','kumar',1000)
print(type(emp1))
print(dir(Employee))
print(emp1.fullName())
print(emp2.fullName())		
'''
#cls


