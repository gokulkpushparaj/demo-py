#lambda function is an anonymous function
#syntax-lambda (x,y):
x=lambda a,b:a+b
print(x(20,20))

x=lambda a,b,c:a*b+c
print(x(1,5,10))

#builtin function
#map and filter
#map function to edit text inside a list
x=["apple","grapes","strawberry","blueberry"]
a=list(map(lambda b:b.upper(),x))
print(a)
#filter function used to fiter a list
a=[10,20,30,40,50]
b=list(filter(lambda c:c>30,a))
print(b)

x=[1,2,3,4,5,6,7,8,9]
b=list(map(lambda c:c**2,x))
print(b)

x=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda k:k%2==0,x))
print(a)

x=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda k:k%2!=0,x))
print(a)

