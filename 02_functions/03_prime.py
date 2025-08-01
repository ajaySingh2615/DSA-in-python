# prime numbers
from math import isqrt

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    
    return True


test_cases = [-10, 0, 1, 2, 3, 4, 5, 9, 11, 15, 17, 25, 29, 100, 101, 9973, 10000]

for num in test_cases:
    result = isPrime(num)
    print(f"{num} : {'prime' if result else 'not prime'}")


# num = int(input("Enter a num to check prime or not: "))

# if isPrime(num) == True:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")