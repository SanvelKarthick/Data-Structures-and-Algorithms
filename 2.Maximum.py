a=[]
length=int(input("Enter the length of the array:"))
for i in range(0,length):
    num=int(input("Enter the number:"))
    a.append(num)
max=a[0]
for j in range(0,len(a)):
    if(max<a[j]):
        max=a[j]
print("Maximum value in the array is",max)
