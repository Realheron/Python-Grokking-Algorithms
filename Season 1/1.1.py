def binary_search(list , item) :
    low = 0 
    high = len(list)
    steps = 0 

    while low <= high :
        mid  = (low + high) // 2 
        guess = list[mid]
        steps += 1 

        if guess == item :
            return mid , steps
        elif guess > item :
            high = mid - 1 
        else :
            low = mid + 1 

    return None , steps


Name_list = [f"Name_{i}" for i in range(128)]

index ,  steps = binary_search(Name_list , "Name_75")

print (f"index: {index}, steps :{steps}")