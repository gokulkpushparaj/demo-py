a={"cat","rat","mat","bat","dat","hat","fat"}
print (a)
print(len(a))
print(type(a))
print("mat" in a)
print("dat" not in a)
for i in a:
    print(i)
    
b={"cat","chit","chat","champ","dat","bat"}
c=a.union(b)
print(c)
d=a.intersection(b)
print (d)
a.add("tat")
print(a)
e=a.difference(b)
print(e)
a.update(b)
print(a)
a.remove("tat")
print(a)
a.pop()
print(a)
a.discard("jet")
print(a)
k=["jet","set","wet","met","get"]
k[4]="bet"
print(k)
m=frozenset(k)
print(m)
m[3]="ggg"
print(m)