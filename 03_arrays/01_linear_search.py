# Linear Search

def linear_search(list1, key):
    for i in range(len(list1)):
        if key == list1[i]:
            return i
        
    return -1


list1 = [2, 4, 6, 8, 10, 12, 14, 16]
key = 10

print(linear_search(list1, key))