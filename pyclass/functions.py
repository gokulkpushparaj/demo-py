#print is a built in funtion
#a function is a block of code, it would work if funtion is called 
#data passed into the function is called parameter
#function is defined as def
#syntax-def funtion name():
def hello():
    print ("good morning")
hello()

def add():
    x=4
    y=9
    z=x+y
    print(z)
add()
#a parameter is a variable 
#parameters is given inside function brackets

def sum(x,y):
    print(x+y)
sum(10,20)

#classifications of arguments
#arbritrary arguments represented as (*args)
#in arbitrary arguments we do not know the number of arguments present in it

def cool(*x):
    print(x[2],x[3])
cool("bear","deer","dog","cat")

def cool(*x):
    print(x[2]*x[3])
cool(22,44,666,78,4,332,22)

#keyword arguments a key=value (format)
def gok(x,y,z):
    print(y+z)
gok(y=10,x=20,z=30)

#arbitrary keyword arguments(kwargs)represented as **kwargs
def abc(**x):
    print(x["a"])
abc(a=6,b=5,c=8)

#default parameter value
def cba(name="gokul"):
    print(name)
cba("abc")
cba()#if a parameter is not given the default parameter will be printed

#return statement
def bbb(x):
    return 10*x
print(bbb(3))#return statement is used to return a value

#pass statements
def beg():
    pass #pass statement is used to pass a funtion without any errors

#recursion
#for a funtion to call itself - works like loop

'''work-find factorial with recursion funtion'''
    