def hash_search(phone_dict , name):
    phone_dict = dict(phone_book) 
    return phone_dict.get(name , None)

phone_book = [
    ("Alice", "123456"),
    ("Bob", "234567"),
    ("Charlie", "345678"),
    ("David", "456789"),
    ("Eve", "567890"),
]

print ("Hash Search:" , hash_search(phone_book, "David"))

