#Programmierübung: Hypotenuse
import math
def hypotenuse(a,b):
   return math.sqrt(a**2+b**2)

#Programmierübung: Die Dreiecke sind rechteckig
def rightTrianglePerimeter(a, b):
   return hypotenuse(a,b) + a + b

#Programmierübung: 2D Distance
def distance2D(x1, y1, x2, y2):
   return hypotenuse(x1-x2, y1-y2)

#Programmierübung: Secure the Perimeter
def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   return distance2D(xA, yA, xB, yB) + distance2D(xB, yB, xC, yC) + distance2D(xA, yA, xC, yC)
