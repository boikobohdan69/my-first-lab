from typing import List

def partition(array: List[int], low: int, high: int) -> int:
    """
    Partition the array based on a pivot element.

    Args:
        array (List[int]): The list of integers to be partitioned.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array: List[int], low: int, high: int) -> None:
    """
    Sort the array in ascending order using the quicksort algorithm.

    Args:
        array (List[int]): The list of integers to be sorted.
        low (int): The starting index of the array or subarray.
        high (int): The ending index of the array or subarray.

    Returns:
        None
    """
    if low < high:
        # Find pivot element such that
        # elements smaller than the pivot are on the left
        # elements greater than the pivot are on the right
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
