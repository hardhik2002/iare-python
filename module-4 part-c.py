from line import *
# PART-C
# 1
str1 = "PyNaTive"
e_s = ""
e_s_ = ""
for i in str1:
    if i.islower():
        e_s = e_s + i
    elif i.isupper():
        e_s_ = e_s_ + i
print(e_s + e_s_)
l()

# 2
def func(str_):
    for i in str_:
        print(i)
str_1=[i for i in input().split("-")]
func(str_1)
l()
# 3
def func1(*x):
    for i in x:
        print(i)
func1(10,20,30)
l()




