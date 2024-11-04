'''a=open("gocool1.txt","x")'''
'''b=open("gocool2.txt","x")'''

a=open("gocool1.txt","w")
b=open("gocool2.txt","w")
txt="hello there "
a.write(txt)
b.write(txt)

a.close()
b.close()

b=open("gocool2.txt","r")
d=b.read()
print(d)
b.close()



