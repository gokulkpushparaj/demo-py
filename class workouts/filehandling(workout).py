"""a=open("gokull.txt","x")"""
b=open("gokull.txt","w")
b.write("futuralabs")
b.close()
c=open("gokull.txt","a")
c.write("\nkochi,palarivattom")
c.close()
d=open("gokull.txt","r")
print(d.read())
d.close()
e=open("gokull.txt","r")
print(e.readline())
print(e.readline())
e.close()
import os
#os.remove()




