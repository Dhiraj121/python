s1=raw_input("Enter the first string")
s2=raw_input("Enter the second string")
a=(set(s1)|set(s2))
for i in a:
    print(i)
	