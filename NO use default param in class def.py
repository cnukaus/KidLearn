Class Student(object):
	def __init__(self,name,course=[]) # THIS IS WRONG as default argument is only evaluated once
		self.course=course
		self.name=name
	def __init__(self,name,course=None) #this is right
		if course is None:
			course=[]
		self.course=course
	def appendcouse(self,coursename)