
def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else :
        max_rest = find_max_recursive(lst[1:])
        return lst[0] if lst [0] > max_rest else max_rest
    

print(find_max_recursive([4, 10, 2, 33, 5]))
