'''x="futura labs cochin has crossed 1 million mark in profits"
print(x)
print(type(x))
print(len(x))
a,b,c="apple","kiwi","orange"
print(a,b,c)
a=11
b=1.11
c=1j
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
o=float(a)
print(o)
p=int(a)
print(p)
q=complex(a)
print(q)
print("is" in x)
print("is"not in x)'''



#odd or even using functions
'''def  oddeven(x):
    if  x % 2 == 0:
        return "Even"
    else:
        return "Odd"
oddeven()'''
    

'''a=int(input("enter a number"))
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")'''

'''x=4
def even():
    print(x%2==0)
even()'''

'''x=int(input("enter a number"))
def even():
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")
even()'''


'''x=[1,2,3,4,5,6,7,8,9,10]
def sum():
   for i in range(1,11):'''
       

'''def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 10
print(getSum(num))'''

a=int(input("enter a number"))

def sumofrange(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    print(sum)
sumofrange(a)
