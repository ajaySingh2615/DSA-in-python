def sub_arrays(arr):
    maximum_sub_array_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j+1):
                print(f"{arr[k]}", end=", " if k!=j else "")
                sum += arr[k]
            if maximum_sub_array_sum < sum:
                maximum_sub_array_sum = sum
            print()
        print()

    return maximum_sub_array_sum

arr = [1, -2, 6, -1, 3]
print(sub_arrays(arr))
