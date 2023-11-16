def DKP(m,W,P,n):
    K=[[0 for X in range(m+1)]for X in range(n+1)]
    for i in range(n+1):
        for w in range(m+1):
            if i==0 or w==0:
                K[i][w]=0
            elif W[i-1]<=w:
                K[i][w]=max(P[i-1]+K[i-1][w-W[i-1]], K[i-1][w])

            else:
                K[i][w]=K[i-1][w]
    return K[n][m]


P=[]
W=[]
n=int(input("Enter the no.of elements:"))
for i in range(n):
    pr=int(input("Enter profit="))
    P.append(pr)
    we=int(input("Enter weight="))
    W.append(we)
m=int(input("Enter maximum weight-"))
maxi=DKP(m,W,P,n)
print("The maximum profit is",maxi)
