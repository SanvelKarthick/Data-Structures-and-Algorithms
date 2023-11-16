def Merge(a,low,mid,high):
    L=a[low:mid+1]
    H=a[mid+1:high+1]
    i=0
    j=0
    k=low
    while((i<len(L))and(j<len(H))):
        if(L[i]<=H[j]):
            a[k]=L[i]
            i=i+1
        else:
            a[k]=H[j]
            j=j+1
        k=k+1
    while(i<len(L)):    
        a[k]=L[i]
        i=i+1
        k=k+1
    while(j<len(H)):
        a[k]=H[j]
        j=j+1
        k=k+1
def MergeSort(a,low,high):
    if(low<high):
        mid=(low+high)//2
        MergeSort(a,low,mid)
        MergeSort(a,mid+1,high)
        Merge(a,low,mid,high)
arr=[]
n=int(input("Enter the length of the array-"))
for i in range(0,n):
    num=int(input("Enter the number-"))
    arr.append(num)
 
print("Before Merge Sort-",arr)
MergeSort(arr,0,n-1)
print("After Merge Sort-",arr)
