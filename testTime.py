#checkes values of time for the prime function

import time, primes

def checkTime(n):
    primes.deletePrime()
    time1 = time.time()
    for i in range(n):
        primes.checkPrime(i)
    return time.time() - time1
        

for j in range(0, 1000000, 1000):
    print(str(j) + ": " + str(checkTime(j)))

input()
