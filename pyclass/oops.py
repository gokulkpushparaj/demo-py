#oops-object oriented programming

#oops concept:-
#class or object
#inheritance
#polymorphism
#data encapsulation
#data abstraction or data hiding

#syntax:-class,classname
'''class sample:
    x=10
obj=sample()
print(obj.x) 
#__innit__ is a built in function used to assign values to object property''' 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

person1=person("john",36)
person2=person("gokul",21)

print(person2.name)
print(person2.age)

#functions inside class is called methods
class person:
    def __init__(self,name,age):

        self.name=name
        self.age=age
    def myfunction(self):
     print("hello my name is"+self.name)
p1=person("gokul",21)
p1.myfunction()
#inheritance is using of methods from a class in differernt class
#inheritance
class person:
    def __init__(self,fname,lname):

        self.firstname=fname
        self.lastname=lname
    def printname(self):
     print(self.firstname,self.lastname)
class student(person):
   pass
x=student("gokul",21)
x.printname()

#types of inheritance

#single inheritance-1 parent class and 1 child class
#multiple inheritance-multiple parent class and one child class
#multi level inheritance-one parentclass, one child class and another inherited child class
#hierarchical inheritance-one parent class and multiple childclass
#hybridinheritance-combination of other inheritance



    

