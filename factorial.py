#take input from user and find the factorial for it
num=int(input("Enter a number:"))
factorial=1
  
if(num<0):
  print("Factorial does'nt exist for Negetive no.s")
  
elif(num==0):
  print("Factorial of 0 is 1")
  
else:
  for i in range(1,num+1):
    factorial=factorial*i
  print"Factorial of ",num,"is",factorial
