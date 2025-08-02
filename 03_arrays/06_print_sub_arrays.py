def print_sub_arrays(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                print(f"{arr[k]}", end=", " if k != j else "")
            print()
        print()

arr = [2, 4, 6, 8, 10]

print_sub_arrays(arr)

# 2
# 2,4
# 2,4,6
# 2,4,6,8
# 2,4,6,8,10

# 4
# 4,6
# 4,6,8
# 4,6,8,10

# 6
# 6,8
# 6,8,10

# 8
# 8,10

# 10