from line import *

# part-b
# 4
m_s = "hardhik"
s_s = "h"
for i in range(len(m_s)):
    if m_s.startswith(s_s, i):
        print(i)
l()
# 5
str_ = "IAREITDEPT"
if len(str_) >= 3:
    if str_.endswith("ing"):
        print(str_ + "ly")
    else:
        print(str_ + "ing")
l()
# 6
if len(str_) >= 2:
    s = str_[0:2] + str_[-2:]
    r = "".join(s)
    print(r)
else:
    pass
l()
# 8
str_2 = input("Enter a string:").lower()
v_l = ["a", "e", "i", "o", "u"]
r = [i for i in str_2 if i not in v_l]
print("".join(r))
l()
# 11
str_3 = "Hardhik"
s = ""
for i in str_3:
    s = i + s
print(s)
l()
# 12
u_string = input("Enter a string:")
c_str = input("Enter the count string:")
count = 0
for i in u_string:
    if i == c_str:
        count = count + 1
print(count)
l()
num = input("Enter a number:")
if num == num[::-1]:
    print("palindrom")
else:
    print("not palindrom")
l()
