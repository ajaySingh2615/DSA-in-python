def reverse_an_array(arr):
    low, high = 0, len(arr)-1

    while low < high:
        # temp = arr[low]
        # arr[low] = arr[high]
        # arr[high] = temp

        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    
    return arr

arr = [2, 4, 6, 8, 10]

print(reverse_an_array(arr))

