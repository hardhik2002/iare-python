# 5
class employee:
    n=int(input("Enter how many employees:"))
    def __init__(self):
        for self.i in range(self.n):
            self.name=input("Enter your name:")
            self.designation=input("Enter your designation:")
            self.salary=int(input("Enter your salary:"))
            print("The employee name is {} his designation is {} and his salary is {}.".format(self.name,
                                                                                               self.designation,
                                                                                               self.salary))


e=employee()

# 6

class person:
    def __init__(self):
        self.name=input("Enter your name:")
        self.year,self.month,self.day=map(int,input("Enter year month number and day with spaces:").split())
        self._year,self._month,self._day=map(int,input("Enter year month number and day of today with spaces:").split())
class dob(person):
    def vote(self):
            self.t_year=self._year-self.year
            if self.t_year>=18:
                print("Eligible")
            else:
                print("Not eligible.")
dob=dob()
dob.vote()
# 7
import math
class circle:
    pi=math.pi
    def area(self):
        self.radius=int(input("Enter the radius:"))
        self.area=self.pi*self.radius**2
        print("Area:",self.area)
    def circumference(self):
        self.circumference=2*self.pi*self.radius
        print("circumference:",self.circumference)
c=circle()
c.area()
c.circumference()






