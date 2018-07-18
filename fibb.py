num=153
div=num%10
digit=num/100
dg=5*1%1000	
result=div*div*div+dg*dg*dg+digit*digit*digit
print(result)
if num == result:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number") 
