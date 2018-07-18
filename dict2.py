def Merge(dict2,dict):
    return(dict.update(dict2))

dict = {'a': 10, 'b': 8}
dict1 = {'c' : 14}
dict2 = {'name': 'Dhiraj'}
print(Merge(dict2,dict))
print(dict)
