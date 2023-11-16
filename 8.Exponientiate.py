num=int(input("Enter the number whose exponential value to be found-"))
n=int(input("Enter the power value:"))
m=n
power=1
x=num
while(m>0):
    while((m % 2)==0):
        m=m//2
        x=x**2
    m=m-1
    power=power*x
print(power)
