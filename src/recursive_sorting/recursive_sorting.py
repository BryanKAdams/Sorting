# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    indexA = 0
    indexB = 0

    for i in range(elements):
        if indexA >= len(arrA) or indexB < len(arrB) and arrA[indexA] > arrB[indexB]:
            merged_arr[i] = arrB[indexB]
            indexB += 1
        else:
            merged_arr[i] = arrA[indexA]
            indexA += 1

    return merged_arr



sort2 = [9, 10, 11, 12, 13]
sort1 = [1, 2, 3, 4, 5]


'''# print(merge(sort1, sort2))
# TO-DO: implement the Merge Sort function below USING RECURSION

# MERGESORT
​
[2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
​
# (base case) If the array is empty or length 1, return
​
# Split the arrays into half
arr1 = [2, 0, 1, 3, 6]
arr2 = [9, 8, 5, 7, 4]
​
# Sort each half
arr1 = [0,1,2,3,6]
arr2 = [4,5,7,8,9]
​
# Merge them back together
# Compare the first values of each array, add smaller of the 2 to result
merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    arr1 = arr[0:len(arr) //2]
    arr2 = arr[len(arr) //2:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)

testArray = [5, 9, 3, 7, 2, 8, 1, 6, 4]
'''
O(nlogn) time complexity
O(n^2) space complexity
'''

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
