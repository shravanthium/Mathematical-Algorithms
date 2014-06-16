#generate prime no.

def prime(n):
    for j in range (2,n):
        for i in range(2,j):
            if j%i==0:
                #print j, 'equals', i, '*', j/i
                break
        else:
            print j, 'is a prime number'


num=int(input("Enter a range: "))
primes=prime(num)
