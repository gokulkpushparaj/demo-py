a=[1,2,3,7,8,4,9,"gokul","kannan","danush"]
a[3]=6
print(a)
a.append("gayathri")
print (a)
a.insert(5,"vismaya")
print(a)
b=["jassim","surya"]
a.extend(b)
print (a)
c=[3,4,5,2,6,8,9,]
c.sort()
print (c)
c.sort(reverse=True)
print(c)
d=b.copy()
print(d)
e=list(a)
print(e)
a.remove("gokul")
print(a)
a.pop(2)
print(a)
a.pop()
print (a)
del a[5]
print (a)
a.clear()
print (a)
del[a]
print (a)