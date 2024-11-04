#two parameters in file handling
#open
# parameterfile
#modeparameter
#modename
#there are 4 modes

#1append or a mode
#2to read r mode
#3x to create
#4 w to write mode
'''a=open("gokul.txt","x")'''
b=open("gokul.txt","w")
b.write("vismaya is my python teacher")
b.close()
c=open("gokul.txt","w")
c.write("seetha is my classmate")
#write mode overwrites the content that was written before
c.close()
x=open("gokul.txt","a") #append method
x.write("\nfutura labs")
x.close()
y=open("gokul.txt","r")#read method
print(y.read())
y.close()
z=open("gokul.txt","r")#reads characters as given
print(z.read(5))
z.close()
k=open("gokul.txt","r")#reads only firstline
print(k.readline())
print(k.readline())
k.close()

