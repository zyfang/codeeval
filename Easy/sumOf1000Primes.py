import sys

sum = 2 #2 is the smallest prime
primes =[2]
for x in xrange(3,3682913):
    if len(primes) == 1000:
        break
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
            sum = sum + x
sys.stdout.write(str(sum))