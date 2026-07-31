
import time

# Selection Sort function
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Assume current element is minimum
        min_index = i

        # Find the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest element with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


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

# Selection Sort
sorted_arr = selection_sort(arr)

# End execution time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("Sorted array:", sorted_arr)
print("Execution time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space        : O(1)")

