sub1=int(input("Enter the sub1 marks:"))
sub2=int(input("Enter the sub2 marks:"))
sub3=int(input("Enter the sub3 marks:"))
sub4=int(input("Enter the sub4 marks:"))
sub5=int(input("Enter the sub5 marks:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
 print("Grade: A")
 
elif(avg>75& avg<90):
    print("Grade:B")
  
elif(avg>50 & avg<75):
    print("Grade:C")
   
elif(avg>35 &avg<50):
    print("Grade:D")
   
else: 
   print("Fail")
   
   