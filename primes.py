import math

primes = [2]

def checkPrime(n):
    if(n < 2): return False
    elif(n == 2): return True
    else:
        i = primes[-1]
        while(not(i >= int(round(math.sqrt(n), 0)))):
            isPrime = True
            for j in primes:
                if(i % j == 0):
                    isPrime = False
                    break
            if isPrime: primes.append(i)
            i += 1
        for j in primes:
            if(j >= n): break
            if(n % j == 0): return False
        return True

def showPrimes():
    print(primes)

def deletePrime():
    primes = [2]
