#generate finbanocci sequence

num=int(input("Enter a no: "))
a, b = 0, 1
print a,
while b < num:
       print b,
       a, b = b, a+b    
