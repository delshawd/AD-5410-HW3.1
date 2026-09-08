####
# Quicksort algorithm taken from:
# https://www.geeksforgeeks.org/quick-sort/
# accessed on 01/25/22
# license: none given
# author: Adnan Aliakbar
###
# CHANGELOG:
# - added if __name__ == "__main__" to driver code
####
# Python3 implementation of QuickSort
# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):

    if start < end:
        p = partition(start, end, array)

        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


if __name__ == "__main__":
    # Driver code
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(0, len(array) - 1, array)

    print(f'Sorted array: {array}')

def selection_sort(A, compare):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if compare(A[min_idx], A[j]):
                min_idx = j

        # Swap the found minimum element with the first element
        A[i], A[min_idx] = A[min_idx], A[i]


# Iterative Quick Sort from:
# https://www.geeksforgeeks.org/python/python-programming-examples/

def partition_iterative(arr, low, high, compare):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if compare(pivot, arr[j]):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr, low, high, compare):
    stack = []

    stack.append(low)
    stack.append(high)

    while stack:
        high = stack.pop()
        low = stack.pop()

        p = partition_iterative(arr, low, high, compare)

        if p - 1 > low:
            stack.append(low)
            stack.append(p - 1)

        if p + 1 < high:
            stack.append(p + 1)
            stack.append(high)

# Iterative Merge Sort from:
# https://www.geeksforgeeks.org/iterative-merge-sort/
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    arr1 = arr[left:left + n1]
    arr2 = arr[mid + 1:mid + 1 + n2]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1

def mergeSort(arr):
    n = len(arr)

    currSize = 1
    while currSize <= n - 1:

        leftStart = 0
        while leftStart < n - 1:

            mid = min(leftStart + currSize - 1, n - 1)
            rightEnd = min(leftStart + 2 * currSize - 1, n - 1)

            merge(arr, leftStart, mid, rightEnd)

            leftStart += 2 * currSize

        currSize = 2 * currSize