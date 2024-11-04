'''def hello():
    print("hello world")
hello()

def addition():
    x=8
    y=9
    z=x+y
    print(z)
addition()

def sum(a,b):
    print(a+b)
sum(30,20)

def abc(*x):
    print(x[2],x[4])
abc(1,2,3,4,5,6,7,8,9)'''

'''x=int(input("enter a number"))
def getsum(x):
    sum=0   
    for i in range(1,x+1):
        if  i%2==0:
            sum+=i    
    print(sum)
getsum(x)'''
#to find factorial
x=int(input("enter a number"))
def getsum(x):
    sum=1
    for i in range(1,x+1):
        sum*=i
    print(sum)
getsum(x)

#to find fibonacci series
x=int(input("enter a number"))
def summ(x):
    a=0
    b=1
    for i in range(x):
        print(a)
        c=a+b
        a=b
        b=c
summ(x)



