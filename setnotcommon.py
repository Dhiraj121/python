s1=raw_input("Enter firststring:")
s2=raw_input("Enter Second string:")
a=list(set(s1)-set(s2))
print("the common letters are:")
for i in a:
    print(i)