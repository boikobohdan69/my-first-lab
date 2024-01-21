from typing import List

def partition(array: List[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array: List[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(array, low, high)
        # Recursive call on the left of the pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of the pivot
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
