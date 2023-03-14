import sys

def list_capacity(lst):
    size = sys.getsizeof(lst) - 64
    if size <= 0:
        return 0
    return (size - 8) // 8

prev_capacity = 0
lst = []

for i in range(64):
    lst.append(i)
    current_capacity = list_capacity(lst)
    if current_capacity != prev_capacity:
        print(f"Capacity changed at element {i}: {prev_capacity} -> {current_capacity}")
        prev_capacity = current_capacity