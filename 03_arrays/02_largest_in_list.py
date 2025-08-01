# largest number

def largest_number(list1):
    largest = list1[0]

    for i in range(1, len(list1)):
        if largest < list1[i]:
            largest = list1[i]
    
    return largest


list1 = [1, 2, 6, 3, 5]

print(f"largest number : {largest_number(list1)}")