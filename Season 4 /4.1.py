def sum_recursive(arr):
    if not arr :
        return 0
    else :
        return arr[0] + sum_recursive(arr[1:])
    
print(sum_recursive([1, 2, 3, 4, 5]))
