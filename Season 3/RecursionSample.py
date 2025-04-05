def look_for_key(box):
    for item in box:
        if isinstance(item, list):  
            look_for_key(item)      
        elif item == "key":        
            print("Found the key!")


my_box = ["item1", ["item2", ["key"]], "item3"]

look_for_key(my_box)
