#Programmierübung: IHOPython
pancakes = int(input())
if pancakes > 3: 
   print('Yum!')
if pancakes <= 3:
   print('Still hungry!')

#Sortierübung: Unerwartete Einrückung
1:    print("message 1")
2: if 2 > 1:
3:   print("message 2")
4: if 1000 < 10:
5:   print("message 3")

#Sortierübung: Unerwartete Ausrückung
1: if 2 > 1:
2:    print("message 1")
3:   print("message 2")
4: if 1000 < 10:
5:   print("message 3")

#Sortierübung: Erwartete Einrückung
1: if 2 > 1:
2: if 1000 < 10:
3:    print("message 1")
4:   print("message 2")
5:   print("message 3")

#Sortierübung: Ordentliche Einrückung
1: if 1000 < 10:
2:    print("message 1")
3: if 2 > 1:
4:  print("message 2")
5:  print("message 3")

#Programmierübung: What's Your Sign?
x=int(input())
if x > 0: 
    print('Positive')
if x == 0:
    print('Zero')
if x < 0:
    print('Negative')

#Multiple-Choice-Übung: Verschachtelte ifs
one line: 'User logged on.'

#Programmierübung: Altersüberprüfer
age = int(input())
if age >= 18:
   print('You can vote')
if  age <18:
 if age >=0:
   print('Too young to vote')
if age < 0:
   print('You are a time traveller')
