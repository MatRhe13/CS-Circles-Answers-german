#Programmierübung: Countup
timeLeft = 1
while timeLeft < 11:
   print(timeLeft)
   timeLeft = timeLeft + 1
print('Blastoff!')

#Programmierübung: One Triangle
n = int(input())
for i in range(0, n):
  X = 0
  for j in range(i, n):
    X = (X * 10) +1
  print(X)

#Programmierübung: Square Census
n = int(input())
for i in range (1, n):
   r = i*i
   if(r < n):
      print(r)

#Programmierübung: Skipping
counter = 0
while True:
  lineIn = input()
  if lineIn=='END':
    break
  if lineIn == 'SKIP':
    continue 
  counter = counter+1
  print('line', counter, '=', lineIn)

#Programmierübung: Faktoren finden
n = int(input())
for a in range(0, (n+1)):
   for b in range(1, (n+1)):
       if a * b == n:
          print(str(a)+ ' times ' + str(b)+ ' equals ' + str(n))
