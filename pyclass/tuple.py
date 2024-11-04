#tuple is also used to store 
#tuple is ordered and indexed
#postion starts from zero
#tuple is unchangable or immutable unlike lists
a=(1,2,6,8,5,"gokul","jazzi","kannan")
print (a)
print (len(a))
print(type(a))
for i in a:
    print(i)

print(a[5])
print(a[3:7])
print(a[3:])
print(a[:5])
print(a[-5:-2])
b=(2,3,6,8,4,7,"abc","cba","gmbh")
c=a+b
print(c)
d=b*4
print(d)
print(d.count(6))
#since we cannot change a tuple and we are desperate, 
# so we are converting tuple to list and making chenges
z=list(a)#converting from tuple to list
print(z)
z.append("zzzz")
print(z)
z.remove("jazzi")
print(z)
z.insert(3,"gocoool")
print(z)
z.pop(4)
print(z)
a=tuple(z)#converting from list to tuple 
print(a)