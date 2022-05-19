def E_or_N(a,b):
    if a==b:
        print("Both are equal")
    elif a>b:
        print("{} is big.".format(a))
    else:
        print("{} is big".format(b))
# calling
a,b=map(int,input().split())
E_or_N(a,b)