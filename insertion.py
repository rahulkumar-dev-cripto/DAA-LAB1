

import time


# Insertion Sort function
def insertion_sort(arr):

    # Start from the second element
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # Move elements greater than key
        # one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Put key in the correct position
        arr[j + 1] = key


# -------- Main Program --------

# Take input from user
numbers = input("Enter numbers separated by spaces: ")

# Convert input into a list of integers
arr = list(map(int, numbers.split()))

print("\nOriginal Array:", arr)

# Start execution timer
start_time = time.perf_counter()

# Apply Insertion Sort
insertion_sort(arr)

# End execution timer
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("Sorted Array:", arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space        : O(1)")

