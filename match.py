import re
count=0
str=raw_input("Any find the string:")
pattern=re.compile(str)
matcher=pattern.finditer('As we know that python learn python')
for match in matcher:
    count+=1
print('match is available:',match.start())
print('The number of occurance:',count)