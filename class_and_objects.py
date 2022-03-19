from line import *
class sample:
    def method1(self,x,y):
        print("self:",self)
        print("x:",x)
        print("y:",y)
#calling
s=sample()
s.method1(10,11)
l()
class dog:
    def __init__(self,name):
        self.name=name
animal=dog("bruno")
print("The animal is:",animal.name)
l()
#accesing attributes/fields
class Dog:
    att1='mammal'
    def __init__(self,name):
        self.name=name
bruno=Dog("bruno")

print("bruno is a {}".format(bruno.__class__.att1))
l()
# Creating class and objects with methods.
class Id:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("My name is:{}".format(self.name))
    #calling
name_=Id("Hardhik")
user_name_=Id("Hardhik1303")
name_.speak()

user_name_.speak()
l()