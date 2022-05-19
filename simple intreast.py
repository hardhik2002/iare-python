def simple_intreast(a,b,c):
    if b=="yes":
        print(float(a*12*b)/100)
    else:
        print(float(a*10*b)/100)
# calling
principal=float(input("Enter the principal ammount:"))
year=float(input("Enter the Number of years:"))
cetizen=input("If you are a senior citizen type yes:").lower()
simple_intreast(principal,year,cetizen)

