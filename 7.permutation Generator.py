def perm(s,k,n):
    if(k==n):
        print(s[0:n])
    else:
        for i in range(k,n):
            temp=s[k]
            s[k]=s[i]
            s[i]=temp
            perm(s,k+1,n)
            temp=s[k]
            s[k]=s[i]
            s[i]=temp
S=list(input("Enter the string of characters:"))
print("The permutations for the given set of characters is:")
perm(S,0,len(S))
