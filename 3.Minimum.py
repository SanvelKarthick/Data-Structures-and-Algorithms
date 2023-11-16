a=[]
length=int(input("Enter the length of the array:"))
for i in range(0,length):
    num=int(input("Enter the number:"))
    a.append(num)
min=a[0]
for j in range(0,len(a)):
    if(min>a[j]):
        min=a[j]
print("Minimum value in the array is",min)
