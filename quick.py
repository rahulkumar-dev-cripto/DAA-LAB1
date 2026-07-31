
import time

# Quick Sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


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

# Quick Sort
sorted_arr = quick_sort(arr)

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
print("Worst Case   : O(n²)")
print("Space        : O(n)")

