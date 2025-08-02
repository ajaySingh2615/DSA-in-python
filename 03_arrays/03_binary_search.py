def binary_search(arr, key):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = low + (high - low) // 2  # prevent overflow

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 4, 6, 8, 10, 12, 14]
key = 8

print(binary_search(arr, key))
