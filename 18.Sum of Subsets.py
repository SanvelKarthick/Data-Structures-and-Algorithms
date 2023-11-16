def SumOfSub(s, k, r):
    x[k]=1
    if(s+W[k]==m):
        print(x[0:k+2])
    elif(s+W[k]+W[k+1]<=m):
        SumOfSub(s+W[k], k+1, r-W[k])
    elif((s+r-W[k]>=m) and (s+W[k+1]<=m)):
        x[k]=0
        SumOfSub(s,k+1,r-W[k])


W=[]
n=int(input("Enter no.of elements:"))
Tot=0
for i in range(n):
    e=int(input("Enter the element-"))
    W.append(e)
    Tot=Tot+e
W.sort()
m=int(input("Enter required sum"))
x=[0]*(n+1)
SumOfSub(0,0,Tot)
