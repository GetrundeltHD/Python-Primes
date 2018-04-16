import time, sys
from primes import *

anz = int(input("Zahl: "))
primeNums = "Alle Primzahlen bis " + str(anz) + ": { "
time1 = time.time()
for i in range(anz):
    if checkPrime(i): primeNums += str(i) + " "
time2 = time.time()
print("\n" + primeNums + "}")
showPrimes()
print("\nTime needed: " + str((time2 - time1)))
input()


