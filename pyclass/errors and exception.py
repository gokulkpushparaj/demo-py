#there are two blocks
#try -try block tests the code 
#except-except block handles the code
#others

#else
#finally

#print(x)
'''try:
    print(x)
except:
    print("an error is there")'''

"""try:
    print(x)
except NameError:
    print("check if variable is correct")
except:
    print("an error occured")"""

try:
    print("x")
except:
    print("an error occured")
else:
    print("everything is fine")
finally:
    print("the program is successfully completed")


#raise is used to throw an error into the program

x=int(input("enter any number"))
if x<0:
    raise Exception("negative numbers are not allowed")
