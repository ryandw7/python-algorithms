# Bubble Sort
import time
import sys
sys.path.append("./utils")
from runtime_wrapper import runtime_wrapper

def bubble_sort(list):
    # grab final index for outer range
    final_index = len(list)-1
    # reverse loop through each item of list - outer loop
    for pass_num in range(final_index, 0, -1):
        # loop through each item that comes before outer loop index (numbers that come after have already been sorted)
        for i in range(pass_num):
            # check if inner item is greater than next number, swaps if true
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        
    return list

test_list = [34, 7, 92, 45, 19, 88, 2, 65, 73, 26, 
                   56, 11, 39, 90, 81, 4, 48, 60, 23, 29, 
                   77, 1, 99, 53, 18, 84, 42, 5, 12, 36, 
                   66, 97, 13, 70, 30, 21, 100, 69, 79, 25, 
                   83, 87, 44, 3, 40, 14, 93, 37, 10, 62, 
                   64, 91, 55, 15, 38, 78, 16, 98, 71, 46, 
                   72, 50, 35, 57, 8, 22, 86, 32, 75, 17, 
                   94, 33, 41, 59, 24, 6, 95, 49, 20, 34, 
                   76, 80, 52, 67, 74, 9, 61, 54, 68, 14]

start_time = time.time()
bubble_sort(test_list)
end_time = time.time()
run_time = end_time - start_time
run_time = run_time * 1000
print(f"Runtime: {run_time:.4f} milliseconds")

