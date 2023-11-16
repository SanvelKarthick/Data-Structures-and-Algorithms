arr=[]
n=int(input("Enter the length of the array-"))
for i in range(0,n):
    num=int(input("Enter the number:"))
    arr.append(num)
print("Before Insertion Sort:",arr)
for x in range(1,n):
    t=arr[x]
    y=x-1
    while((y>=0)and(t<arr[y])):
        arr[y+1]=arr[y]
        y=y-1
        arr[y+1]=t
print("After Insertion Sort:",arr)
