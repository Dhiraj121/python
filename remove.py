#remove the variable in object
class Remove:
    def __init__(self):
	    self.a=10
		self.b=20
		self.a=30
r1=remove()
r2=remove()
del r1.c
print('r1:',r1.__dict__)
print('r2:',r2.__dict__)

  