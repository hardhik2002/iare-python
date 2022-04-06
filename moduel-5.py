# PART-B
# 1
class coordinates1:
    def __init__(self):
        self.x1,self.x2=map(float,input("Enter x coordinates:").split())
        self.y1,self.y2=map(float,input("Enter y coordinates:").split())
class midpoint(coordinates1):
    def mid_point(self):
        print(((self.x2+self.x1)/2)+(self.y2+self.y1)/2)

mid=midpoint()
mid.mid_point()

# 2
class numbers:
    def __init__(self):
        self.lst=[int(i) for i in input().split()]
    def max_num(self):
        self.max=max(self.lst)
        print("The max is:",self.max)
num=numbers()
num.max_num()
# 4
class rectangle:
    l,b=map(float,input("Enter length and breadth of a rectange:").split())
    def area(self):
        print("area is:",self.l*self.b)
area_rectangle=rectangle()
area_rectangle.area()
# 3
class student:
    def __init__(self):
        self.name=input("Enter your name:")
        self.roll=input("Enter your roll number:")
        self.marks=int(input("Enter 3 subjects marks total:"))
    def display(self):
        print("Your name is {} and roll number is {} your marks are {}.".format(self.name,self.roll,self.marks))
stu=student()
stu.display()










