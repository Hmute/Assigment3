import json
import time
import matplotlib.pyplot as plt

# Load the array and the search tasks
with open('ex2data.json') as f:
    array = json.load(f)
with open('ex2tasks.json') as f:
    tasks = json.load(f)

# Binary search algorithm with configurable initial midpoint
def binary_search(array, target, start, end, mid):
    if start > end:
        return False

    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end, (mid + 1 + end) // 2)
    else:
        return binary_search(array, target, start, mid - 1, (start + mid - 1) // 2)

# Time the performance of each search task with different midpoints
results = []
for task in tasks:
    start = 0
    end = len(array) - 1
    first_mid = array[start]
    middle_mid = array[(start + end) // 2]
    last_mid = array[end]

    # Measure execution time with first midpoint
    start_time = time.time()
    binary_search(array, task, start, end, (start + end) // 2)
    first_time = time.time() - start_time

    # Measure execution time with middle midpoint
    start_time = time.time()
    binary_search(array, task, start, end, middle_mid)
    middle_time = time.time() - start_time

    # Measure execution time with last midpoint
    start_time = time.time()
    binary_search(array, task, start, end, (start + end) // 2)
    last_time = time.time() - start_time

    # Choose the midpoint with the best performance
    if first_time <= middle_time and first_time <= last_time:
        best_mid = first_mid
    elif middle_time <= first_time and middle_time <= last_time:
        best_mid = middle_mid
    else:
        best_mid = last_mid

    results.append((task, best_mid))

# Create a scatter plot to visualize the results
x = [r[0] for r in results]
y = [r[1] for r in results]
plt.scatter(x, y)
plt.xlabel('Search Tasks')
plt.ylabel('Best Midpoint')
plt.title('Binary Search with Different Initial Midpoints')
plt.show()
