x={"name":"gokul","age":21,"place":"ijk","gender":"male"}
print(x)

print(type(x))

print(len(x))

print(x["gender"])

print(x.get("place"))

print(x.keys())

print(x.values())

print(x.items())

print("gender" in x)

print("gender" not in x)

for i in x:
    print(i)

for i in x:
    print(x[i])  

for i in x.keys():
    print(i)

for i in x.values():
    print(i)

for i  in x.items():
    print (i)

x["age"]=25
print(x)

x["profession"]="data analyst"
print(x)

x.update({"ugcompletion":"calicut university"})
print(x)

y=x.copy()
print(y)

x.pop("age")
print(x)

x.popitem()
print(x)

del x ["name"]

x.clear()
print(x)