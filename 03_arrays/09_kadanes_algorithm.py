def kadanes(numbers):
    # ms = float('-inf')
    # cs = 0
    # n = len(numbers)

    # for i in range(n):
    #     cs = cs + numbers[i]
    #     if cs < 0:
    #         cs = 0

    #     ms = max(cs, ms)

    # return ms

    cs = ms = numbers[0]

    for i in range(1, len(numbers)):
        cs = max(numbers[i], cs + numbers[i])
        ms = max(ms, cs)
    return ms


numbers = [-2, -3, 4, -1, -2, 1, 5, -3]
numbers = [-2, -3, -4, -1, -2, -1, -5, -3]
print(kadanes(numbers))
