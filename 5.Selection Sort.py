arr=[]
n=int(input("Enter the length of the array-"))
for i in range(0,n):
    num=int(input("Enter the number:"))
    arr.append(num)
print("Before Selection Sort:",arr)
for x in range(0,n):
    y=x
    for z in range(x+1,n):
        if(arr[z]<arr[y]):
            y=z
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp
print("After Selection Sort:",arr)
