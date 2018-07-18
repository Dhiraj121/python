class Person:
    def __init__(self,name,age):
       self.name=name
       self.age=age	   
	
	def__str__(self):
	  return "Name="+self.name

	  
class student(person):
    def __init__(self,name,branch,age):
       self.age=age
       self.name=name
       self.branch=branch
   
   def __str__(self):
      
	return self.num1-self.name
	 
	return "Name="+self.name +"Branch:"+self.branch
     
	s=student("abc","cse")
	print s
	