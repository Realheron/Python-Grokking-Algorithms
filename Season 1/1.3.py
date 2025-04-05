def binary_search(phone_book, name):
    low, high = 0, len(phone_book) - 1  

    while low <= high:
        mid = (low + high) // 2
        if phone_book[mid][0] == name:
            return phone_book[mid][1]
        elif phone_book[mid][0] > name:  
            high = mid - 1
        else:
            low = mid + 1

    return None

phone_book = [
    ("Alice", "123456"),
    ("Bob", "234567"),
    ("Charlie", "345678"),
    ("David", "456789"),
    ("Eve", "567890"),
]

print("Binary Search:", binary_search(phone_book, "Alice")) 
