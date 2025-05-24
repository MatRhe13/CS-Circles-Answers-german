#Multiple-Choice-Übung: Das letzte Zeichen
S[len(S)-1]

#Programmierübung: Strings Rasieren
S=input()
print(S[1:-1])

#Programmierübung: Heads and Tails
x = input ()
y = x[-1]
z = x[0]
a = x[1:-1]
print(y+a+z)

#Programmierübung: Next Letter
string = input()
if string == "Z":
   print("A")
   
if string != "Z":
      print(chr(ord(string) +1))

#Programmierübung: Pig Latin
x = input()
print(x[1:len(x)]+x[0]+"ay")

#Programmierübung: The Name Game
x = input()
print (x+",",x+",","bo-b"+x[1:len(x)])
print ("banana-fana fo-f"+x[1:len(x)])
print ("fee-fi-mo-m"+x[1:len(x)])
print (x+"!")
