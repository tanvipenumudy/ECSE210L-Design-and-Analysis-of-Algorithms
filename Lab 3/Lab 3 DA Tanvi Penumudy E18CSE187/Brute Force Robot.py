import random
T=[]
for j in range(8):
    column=[]
    for i in range(8):
        column.append(0)
    T.append(column)
r=[-1,1]
a=[1, -1, -1, 1, 1, 1 -1, 1]
n=len(a)
for i in range(n):
  for j in range(n):
    if(i==j):
      T[i][j]=0
    elif(a[i]==1 and a[j]==1):
      T[i][j]=1
    elif(a[i]==1 and a[j]==-1):
      T[i][j]=-1
    else:
      z=random.randint(0,1)
      T[i][j]=r[z]
print(T)
res=[]
for i in range(n):
  sum=0
  for j in range(n):
    sum+=T[i][j]
  if(sum>0):
    print(i)