class MyException(Exception):
    def __init__(self,mesg):
	    self.mesg
	
	def __str__(self):
	   return "Exception occured:"+self.msg
	   
try:
    raise MyException("Test Exception")
except MyException as e:
    print e