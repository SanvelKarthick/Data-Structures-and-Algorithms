def Partition(a,x,y):
    v=a[y]
    i=x-1
    for j in range(x,y):
        if(a[j]<=v):
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[y]=a[y],a[i+1]
    return i+1

def QuickSort(a,I,l):
    if(I<l):
        P=Partition(a,I,l)
        QuickSort(a,I,P-1)
        QuickSort(a,P+1,l)
arr=[]
n=int(input("Enter the length of the array-"))
for i in range(0,n):
    num=int(input("Enter the number-"))
    arr.append(num)
 
print("Before Quick Sort:",arr)
QuickSort(arr,0,n-1)
print("After Quick Sort:",arr)
