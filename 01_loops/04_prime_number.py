# prime number
from math import sqrt

num = int(input("enter a number: "))

isPrime = True

for i in range(2, sqrt(num)+1):
    if num % i == 0:
        isPrime = False
        break

print(f"{'true' if isPrime else 'false'}")