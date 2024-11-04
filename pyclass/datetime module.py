#date time module is used to fetch date and time


import datetime

x=datetime.datetime.now()
print (x)
print(x.strftime("%a")) #prints as WED
print(x.strftime("%A"))#prints as wednesday
print(x.strftime("%B"))#prints OCTOBER
print(x.strftime("%b"))#oct
print(x.strftime("%y"))#prints year in short 24
print(x.strftime("%Y"))#prints year long 2024
print(x.strftime("%D"))#prints full date mm/dd/yy
print(x.strftime("%H"))# 
print(x.strftime("%I"))#to check what hour (24h format)
print(x.strftime("%p"))#to check am or pm

y=datetime.datetime(2002,4,12)
print(y.strftime("%A"))


