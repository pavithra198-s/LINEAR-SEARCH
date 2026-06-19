def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   
    return -1          
numbers = [10, 25, 30, 45, 50]

result = linear_search(numbers, 30)
if result != -1:
    print("ELEMENT FOUND AT ",result)
else:
    print("ELEMENT NOT FOUND -1")