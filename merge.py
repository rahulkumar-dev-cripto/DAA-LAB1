
import time

# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Merge two sorted arrays
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# User input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("\nOriginal array:", arr)

# Start execution time
start_time = time.perf_counter()

# Merge Sort
sorted_arr = merge_sort(arr)

# End execution time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("Sorted array:", sorted_arr)
print("Execution time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
print("Space        : O(n)")

