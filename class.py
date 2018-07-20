class Student:
    def __init__(self,n,roll,marks):
	    self.name=n
		self.roll=roll
		self.marks=marks
	def display(self):
	    print('Student Name:',self.name)
		print('Student RollNo:',self.roll)
		print('Student Marks:',self.marks)
		
s1=Student("Dhiraj",1,56)
s2=Student("Ravi",2,36)
s3=Student("Vinay",3,45)
s1.display()
s2.display()
s3.display()
print(s1.__dict__)