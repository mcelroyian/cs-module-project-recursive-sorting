# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i_of_A = 0
    i_of_B = 0
    #As long as there are still items in one of the arrays
    while i_of_A < len(arrA) and i_of_B < len(arrB):
        #Add from Array A if we reached the end of Array B or 
        #the current item in Array A is smaller
        if i_of_B == len(arrB) or arrA[i_of_A] <= arrB[i_of_B]:
            merged_arr.append(arrA[i_of_A])
            i_of_A += 1
        #Otherwise add from Array B
        else:
            merged_arr.append(arrB[i_of_B])
            i_of_B += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

