""" Traditional Method to generate prime no.
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
"""

def get_primes(n):
	numbers=set(range(n,1,-1))
	primes=[]
	while numbers:
		p=numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return primes
