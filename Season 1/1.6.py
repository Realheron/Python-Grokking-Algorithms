

phone_book = [
    ("Alice", "135659"),
    ("Bob", "4578213"),
    ("Charlie", "468769"),
    ("David", "4651358"),
    ("Eve", "1254687"),
    ("Heron", "589746"),
]

a_names = [numbers for name , numbers in phone_book if name.startswith("A")]

print("numbers of names starting with 'A' :", a_names)