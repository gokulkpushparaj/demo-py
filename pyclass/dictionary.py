#dictionary is ordered, changable and allows duplicate values
#curly brackets are used for dictionary
#instead of position keys are used
x={"name":"gokul","age":21,"place":"irinjalakuda","gender":"male","yob":2002}
print(x)
print(type(x))
print(len(x))
print(x["yob"])
print(x.get("gender"))
print(x.keys())
print(x.values())
print(x.items())
print("gender" in x)
print("age" not in x)
for i in x:
    print(i)
for i in x:
    print(x[i])

for i in x.keys():
    print(i)

for i in x.values():
    print(i)

for i in x.items():
    print(i)

#to change a key you can use this method

x["age"]="35"
print(x)

x.update({"age":91,"place":"cochin"})
print(x)
 
x["profession"]="data analyst"
print (x)

x.update({"ug completion":"calicut university"})
print(x)

y=x.copy()#copy method as said in earlier classes
print(y)

z=dict(x) #we can also use dict method to copy from one variable to another
print(z)
#remove method
x.pop("place")
print (x)

#pop item method(REMOVAL)
x.popitem()
print(x)

'''del x["age"]
print(x)

x.clear()
print(x)

del x
print(x)''' #commented for understanding 

