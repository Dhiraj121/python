d = {'a':22,'b':34,'c':3,'d':4}
print("Dictionary")
print(d)
key=raw_input("Enter the delete key:")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)