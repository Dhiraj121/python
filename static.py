class Static:
    a=10
	def __init__(self):
	    self.b=20
		Static.c=30
	
	def d1(self):
	    self.d=40
		Static.e=50
		@method of class
	def d2(cls):
	    cls.f=50
		Static.g=60

s=Static()
s.d1()
Static.d2()
		

print(Static.__dict__)
