X=[[2,5],
  [4,5]]

Y=[[5,4],
  [6,8]]

result=[[0,0],
        [0,0]]

for i in range(len(X)):
   for j in range(len (X[0])):
       result[i][j]=X[i][j]*Y[i][j]
for r in result:
    print(r)
	
   