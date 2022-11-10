lst=[int(i) for i in input("Enter numbers with spaces:").split()]
print("unsorted list:",lst)
for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("sorted list:",lst)