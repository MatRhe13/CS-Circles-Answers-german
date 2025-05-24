#Programmierübung: Eggsactly
eggs=int(input())
print(eggs//12)
print(eggs%12)

#Programmierübung: Teilbarkeit
a=int(input())
b=int(input())
if a % b == 0:
   divisibility = "divisible"
else:
   divisibility = "not divisible"
print(divisibility)

#Programmierübung: Pizza Circles
r=float(input())
import math
a=math.pi*r**2
print(a)

#Programmierübung: Geometrisches Mittel
a=float(input())
b=float(input())
z=a*b
z=z**(1/2)
print(z)

#Kurzübung: Operatorrangfolge
4

#Programmierübung: Klammer-Test
a=int(input())
b=int(input())
c=int(input())
print((a+b)*c)

#Programmierübung: A Feat With Feet
f=float(input())
print(f*30.48)

#Programmierübung: Erdanziehungskraft
v=float(input())
import math
a = -4.9
b = -v
c = 11000
wurzel = math.sqrt(b**2 - 4 * a * c)
t = (-b - wurzel) / (2 * a)
print(t)
