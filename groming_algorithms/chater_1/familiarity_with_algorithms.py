from math import ceil

def binary_search(massive, index):
    low = 0 
    high = len(massive) - 1

    while low <= high:
        mid = ceil((low + high) / 2)
        guess = massive[mid] 
        if guess == index:
            return mid
        if guess > index:
            high = mid - 1
        else:
            low = mid + 1
    return None 


