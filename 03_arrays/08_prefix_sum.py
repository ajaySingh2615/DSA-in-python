def prefix_sub_array_sum(arr):
    curr_sum = 0
    maxSum = arr[0]
    
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    # Create prefix sum array
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + arr[i]

    # Loop to find max subarray sum using prefix sum

    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix[j] if i == 0 else prefix[j] - prefix[i-1]

            if maxSum < curr_sum:
                maxSum = curr_sum
    
    return maxSum

arr = [1, -2, 6, -1, 3]
print(prefix_sub_array_sum(arr))

