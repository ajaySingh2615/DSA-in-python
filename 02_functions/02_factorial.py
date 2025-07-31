def factorial_of_num(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

num = 5

print(f"factorial of {num} is {factorial_of_num(num)}")