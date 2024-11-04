#set is given inside curly brackets
#set is unordered, unindexed and unchangable, but new items can be added and removed
#set does'nt allow duplicate values
#
a={1,5,7,33,6,77,4,"abc","ccc","kkk","arc"}
print(a)#since set is unindexed, when printing,it prints unorderd
print(type (a))
print(len(a))
for i in a:
    print(i)

print ("kkk" in a)
print ("kkk" not in a )
#add method 
a.add("ooo")
print (a)
#update method- to add another set
b={1,2,5,6,3,7,9,8,0,4,"egg","duck"}
a.update(b)
print(a)
#since set does'nt allow duplicate items it cancells out the repeated values 
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e={"dac","aoc","cid",22,45,6,7,78,545,1,3,77}
f=a.intersection(e)
print(f)
g=a.difference(e)#cancells out the common items and displays items only from {a}
print(g)
#remove method
a.remove("arc")
print(a)
#we can use discard method to avoid errors tho if we use remove method it becomes error
b.discard("bond")
print(b)
#pop method in set deletes a random item from the set
e.pop()
print (e)
#clear method clears the entire set
e.clear()
print (e)
del b
g=["cat","rat","mat","pat","chat"]
print(g)
g[2]="hat"
print(g)
z=frozenset(g)
print(z)
z[3]="fat"#frozen set doesn't allow item assignment
print(z)
