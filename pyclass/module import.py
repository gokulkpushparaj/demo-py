import modules
print(modules.add(10,20))
import math

print(max(1,2,3,4,5,56,6,7,8,9))
print(min(1,2,3,4,5,6,7,8,9,99))
#returning absolute value that  if given a negative number it becomes a positive number
print(abs(-30))
#squaring
print(pow(2,3))

print(math.pi)
print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(873.3534564))
print(math.floor(87.27856))

print(modules.devision(90,9))
print(modules.multiplication(1,10))
print(modules.substraction(100,36))


def areaofcircle(radius):
    return math.pi*radius**2
radius=float(input("enter the radius of the circle"))
area=areaofcircle(radius)
print("area of the circle is",area)

r=int(input("enter radius"))
print(math.pi*r*r)

r=int(input("enter the radius of the cylinder"))
h=int(input("enter the height of the cylinder"))
print(math.pi*r*r*h)