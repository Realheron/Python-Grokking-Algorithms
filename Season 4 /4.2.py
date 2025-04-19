
def count_items(lst):
    if not lst:
        return 0
    else:
        return 1 + count_items(lst[1:])

print(count_items([10, 20, 30, 40]))
