def fact(n):
    if n==1:
      return n
    else:
      return n*fact(n-1)
n=int(input ("enter your fact number:"))
if n==0:
      print ("the factorial of 0 is 1")
elif n<0:
      print ("the given factorial number is negative")
else:
      print("The factorial number of",n, "is",fact(n))