def linear_search(phone_book, name):
    for contact in phone_book:
        if contact[0] == name:
            return contact[1]
    return None

phone_book = [
    ("Alice", "123456"),
    ("Bob", "234567"),
    ("Charlie", "345678"),
    ("David", "456789"),
    ("Eve", "567890"),
]


print("Linear Search:", linear_search(phone_book, "David")) 
