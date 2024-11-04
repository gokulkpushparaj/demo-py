x="cats vs dogs"
for i in x:
    print(i)

y=["cats","dogs","bats","vampires"]
for i in y:
    print(i)

z=("car","bike","bus","auto")
print(type(z))
for i in z:
    print(i)

a={"jeep","bmw","mercedes","vw"}
print(type(a))
for i in a:
    print (i)

b={"brand":"bmw","found":1920,"by":"gokul","place":"germany"}
print(type(b))
for i in b:
    print(i)
  
for i in b.keys():
    print(i)

for i in b.values():
    print(i)

for i in b.items():
    print(i)

for i in range(11):
    print(i)


for i in range (1,11,2):
    print(i)

for i in range (1,11):
    if i==5:
        break
print(i)

for i in range (1,11):
    if i==5:
        continue
    print(i)

x=[1,2,3,4]
y=["a","b","c","d"]
print(type(x))
for i in x:
    for j in y:
        print(i,j)

'''k=[1,2,3,4,5,6,7,8,9,10]
for i in k:
    i++k
    print(i)'''


k= [1, 2, 3, 4, 5,6,7,8,9,10]
sum = 0
for i in k:
    sum += i
print(sum)

k=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(1,11):
    if i%2==1:
        sum +=i
    print(sum)

'''add 
fibonacci series
factorial'''

m=[1,2,3,4,5,6,7,8,9,10]
a,b=1,2
sum=0
for i in range (1,11):
    sum+=i
    print()
