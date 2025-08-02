def pairs_in_an_array(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            print(f"({arr[i]}, {arr[j]})")


arr = [2, 4, 6, 8, 10]

pairs_in_an_array(arr)

# (2, 4), (2, 6), (2, 8), (2, 10)
# (4, 6), (4, 8), (4, 10)
# (6, 8), (6, 10)
# (8, 10)