import time


def binary_search(sorted_list, target):

   
    # low = low if low else 0
    # high = high if high else high in sorted_list[len(sorted_list)-1]
    low = 0
    high = len(sorted_list)
    mid = low + high // 2

    if sorted_list[mid] == target:
        return mid #index of number we want (target)
    
    elif sorted_list[mid] > target:
        sorted_list = sorted_list[:mid]
        return binary_search(sorted_list, target)

    elif sorted_list[mid]:
        sorted_list = sorted_list[mid:]
        return binary_search(sorted_list, target)

    return None
    

my_list = [1,3,5,7,9]

start_time = time.time()
   
print(binary_search(my_list,3)) #=> 1

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")