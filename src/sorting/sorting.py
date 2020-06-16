# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0

    while (i < len(arrA)) and (j < len(arrB)):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1
    
    while j < len(arrB):
        merged_arr.append(arrB[j])
        i += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case is if the length of the array is less than or equal to 1,
    # then the array is already sorted and we should return the array. 
    # otherwise we need to divide the array in two halves and run the merge function
    # on the two halves. We will also need to recursively call the merge sort on those merged array.

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

