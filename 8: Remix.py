#Programmierübung: Python Adder
S= input()
n= 0
for position in range(0, len(S)):
   if S[n:(n+1)] == "+":
      b= int(S[0:n])
      c= int(S[n:len(S)])
      print(c+b)
   n=n+1

#Programmierübung: Substring Counting
S = input()
b = input()
n = 0
d = 0
for position in range(0, len(b)):
   if S == b[n:len(S)+n]:
      d = d+1
   n = n+1
print(d)

#Programmierübung: Watch the Pendulum
L = float(input())
A = float(input())
import math
t = 0
for t in range (0,10):
   x = (L*math.cos(A*(math.cos((t*(math.sqrt(9.8/L))))))-L*math.cos(A))
   print(x)

#Programmierübung: Centering Text
width = int(input())
a = input()
for i in range(0,4):
   width1 = (width-(len(a)))//2
   width2 = int(width-width1-len(a))
   points ="."
   print(points*width2+(a)+points*width1)
   if a != "END":
      a = input()
   if a == "END":
      break

#Programmierübung: Ending Time
starting_time = input()
D = int(input())
H = int(starting_time[0:2])
M = int(starting_time[3:5])
if D + M > 59:
    H = H + (D + M) // 60
    M = (D + M) % 60
    if len(str(M)) == 1:
        M = '0' + str(M)
    if H > 23:
        H = H % 24
        if len(str(H)) == 1:
           H = '0' + str(H)
print(str(H) + ':' + str(M))

#Programmierübung: Character Map
print("chr:      !   \"   #   $   %   &   '   (   )   *   +   ,   -   .   / ")
print("asc: 32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 ")
print("chr:  0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ? ")
print("asc: 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63 ")
print("chr:  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O ")
print("asc: 64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79 ")
print("chr:  P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _ ")
print("asc: 80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95 ")
print("chr:  `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o ")
print("asc: 96  97  98  99  100 101 102 103 104 105 106 107 108 109 110 111")
print("chr:  p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~   "+(chr(127)))
print("asc: 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 ")
