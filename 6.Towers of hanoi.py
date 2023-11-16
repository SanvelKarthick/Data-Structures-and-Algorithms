def TOH(n,x,y,z):
    if(n>=1):
        TOH(n-1,x,z,y)
        print("Move top disk from tower",x,"to top of tower",y)
        TOH(n-1,z,y,x)
ndisk=int(input("Enter the no.of disks:"))
TOH(ndisk,'A','B','C')
