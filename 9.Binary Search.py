arr=[]
n=int(input("Enter the array length:"))
for i in range(0,n):
    num=int(input("Enter the number:"))
    arr.append(num)
x=int(input("Enter value to be searched"))
l=0
h=n
while(l<(h-1)):
    m=(l+h)//2
    if x<arr[m]:
        h=m
    else:
        l=m
if(x==arr[l]):
    print(x,"is found at position",l,"in the array")
else:
    print(x,"is not in the array")
