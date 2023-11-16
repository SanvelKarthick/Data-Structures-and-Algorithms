n=int(input("Enter the array length:"))
arr=[]
for i in range(0,n):
    num=int(input("Enter the number:"))
    arr.append(num)
x=int(input("Enter the value to be searched:"))
j=0
while(j<=n-1):
    if(arr[j]==x):
        print(x,"is present at index position",j,"in the array")
        break
    j=j+1
else:
        print(x,"is not in the array")
