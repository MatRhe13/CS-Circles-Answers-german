#Multiple-Choice-Übung: Meta-Kram
[2, 25, 12, 12]

#Programmierübung: Monkey in the Middle
def middle(L):
      return L[int(len(L)/2)]

#Programmierübung: It's Natural
def naturalNumbers(x):
    a = []
    for i in range(1, x + 1):
        a += [i]
    return a

#Programmierübung: Palindrome
def isPalindrome(S):
    if str(S) == str(S)[::-1]:
        return True
    else:
        return False

#Programmierübung: Product
def prod(L):
    a = 1
    for i in range(0, len(L)):
        a *= L[i]
    return a

#Programmierübung: for in
def prod(L):
   total = 1
   for x in L:
      total*=x
   return total

#Kurzübung: Mystery Function
3

#Sortierübung: à la Mode
1: def mode(L):
2:     frequency = [0] * 10
3:     for i in L:
4:         frequency[i] += 1
5:     for i in range(0, 10):
6:         if frequency[i] == max(frequency):
7:             return i
