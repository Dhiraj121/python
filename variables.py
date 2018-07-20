class Variables:
    a=10  #static variables
	def __init__(self):
	    self.b=20  #instance variables
v1=Variables()
print(v1.a,v1.b)
print(Variables.a,v1.b)


