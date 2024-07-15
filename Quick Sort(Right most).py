def quickSort(array, first, last):
    if first < last:
        p = partition(array, first, last)  # partition the array and get the index of the pivot element
        quickSort(array, first, p - 1)
        quickSort(array, p + 1, last)

def partition(array, first, last):
    pivot = array[last]
    i = first - 1

    for j in range(first, last):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last] = array[last], array[i + 1]
    return i + 1

array = [45, 22, 9, 18, 235, 74, 8]
print("Unsorted array: ", array)

n = len(array)

quickSort(array, 0, n - 1)
print()

print("Sorted array: ", array)
