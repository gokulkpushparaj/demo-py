a=[1,2,"b","c","hhh",77,"vismaya"]
print (a)
print(type(a))
print(len(a))
print(a[1])
print (a[2:5])
print(a[:3])
print(a[-1])
print(a[-5:-2])
print(a[-2:])
print(a[:-5])
for i in a:
    print (i)

print("vismaya" in a )
print("vismaya" not in a )
print("gokul" not in a )
print("gokul" in a )
a[2]="j"#replacing method in list
print(a)
a.append("abc")#to add new items to the list "adds to the last position"
print(a)
a.insert(4,"cab")#similar to append but position based method
print(a)
b=["bbb","nnn","hhh",1,2,4,5,6]
a.extend(b)#method to join two lists
print(a)
c=[1,7,4,3,6,8,10]
c.sort()#to sort a list
print(c)
c.sort(reverse=True)#sorted list will be reversed
print(c)
d=c.copy()#copy method copies list from a variable and stores it in another
print(d)
h=list(a)#another way of copying
print(h)
z=b+c#using arithmetic operator to add two strings to a variable
print(z)
print (a.count(1))#count method
a.remove("hhh")#remove method 
print(a)
a.pop(3)#similar to remove method but postion based
print(a)
a.pop()#if given without postion it removes the last position 
print(a)
del a[4]#delete is a keyword used to delete a postion 
print(a)
a.clear()#clear method clears out the entire item in the list but the list will still be there
print(a)
del a #deletes the list
print (a)
