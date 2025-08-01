# prime numbers
from math import isqrt

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    
    return True


num = int(input("Enter a num to check prime or not: "))

if isPrime(num) == True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")