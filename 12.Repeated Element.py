arr=[]
n=int(input("Enter the length of the array:"))
for x in range(0,n):
    num=int(input("Enter the number:"))
    arr.append(num)
rep=[]
for i in range(0,n):
    k=i+1
    for j in range(k,n):
        if(arr[i]==arr[j] and arr[i] not in rep):
            rep.append(arr[j])
print("Repeated elements in given array: ",rep)
