num = 432

reverse_num = 0

while num > 0:
    lastDigit = num % 10
    reverse_num = lastDigit + (reverse_num * 10)
    num //= 10

print(f"reverse number is {reverse_num}")