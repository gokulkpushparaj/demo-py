a="python, is, a, programming, language"
print(a)
print(len(a))#len funtion counts the letter ina string membership operator (in , not in) function is used below
print(a[1])
print("is" in a)
print("hd" in a)
print("hd" not in a)
print("is" not in a)
for i in a:
    print(i)
    
print(a[10:20]) #slicing:cutting out from a statement
print(a[:25])
print(a[20:])
print(a[-15:])#negative indexing is used to find the last index
print(a.lower())#upper and lower methods used to make lower case and uppercase 
y="         gokul"
print(y.strip())  #you can use strip method to clear out the space nb:like above used before the name
print(a.replace("python","java"))#replace method is used to replace a word with another word
print(a.split(","))#used to split between given characters
print(a.count("a"))#used to count letters or characters
print(y+a)
g=3
o=f"my name is arun iam{g}"#string formatting using f-string
print(o) #you dont need to add two variables since g is given in the curly brackets
z="goodmorning\n have a niceday" #/n is used to break down to the next line
print(z)
