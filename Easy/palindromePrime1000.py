import sys

def ispalin(x):
    "returns true if x is a palindrome, false otherwise"
    listx = list(x)
    for i in range(len(listx)/2):
        if listx[i] != listx[-(i+1)]:
            return False
    return True            

primes =[2] #store primes (for determining primes)
largest_palin = 2
for x in xrange(3,1000):
    if x % 2 == 0:
        continue
    else:
        prime = True
        maxdiv = x**0.5
        for xdiv in primes:
            if xdiv > maxdiv:
                break
            if x % xdiv==0:
                prime = False
                break
        if prime:
            primes.append(x)
            if ispalin(str(x)):
                largest_palin = x
sys.stdout.write(str(largest_palin))