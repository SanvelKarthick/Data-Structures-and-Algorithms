import random


def Prime(n):
    q=n-1
    for i in range(n+1):
        m=q
        y=1
        a=random.randrange(n-1)%q+1
        z=a
        while(m>0):
            while(m%2==0):
                z=z**2 % n
                m=m/2
            m=m-1
            y=(y*z)%n
        if(y!=1):
            return False
    return True

n=int(input("Enter a number:"))
res=Prime(n)
 
if res==True:
    print("Prime")
else:
    print("Not a Prime")
