# I used this for the iterative Binary Search:
# https://www.geeksforgeeks.org/binary-search/
# Python3 code to implement iterative Binary Search.
# It returns location of x in given array arr
# if present, else returns -1

def binary_search_sub(arr, l, r, x):

    mid = 0  ### new line
    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid  ### new line

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present so return the last midpoint chosen
    return mid  ### new line


if __name__ == "__main__":
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binary_search_sub(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")