def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 6, 2, 10]
print(linear_search(arr, 6))  # Output: 2
