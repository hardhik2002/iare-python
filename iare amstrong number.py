n=int(input("Enter a number to know weather it is amstrong or not:"))
ord=len(str(n))
i=0
s=0
temp=n
while temp!=0:
    digit=temp%10
    s=s+(digit**ord)
    temp=temp//10
if s==n:
    print("It is an amstrong number")
else:
    print("It is not a amstrong number")


