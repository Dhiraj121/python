d={'Dhiraj':1,'Gadekar':2,'Pune':3}
key=raw_input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")