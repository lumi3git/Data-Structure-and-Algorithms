def selectionSort(array,size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            if array[i] > array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [50,85,23,-41,25]

unsorted_data = data.copy()

size = len(data)

selectionSort(data ,size)

print("Unsorted Array is:")
print(unsorted_data)

print("\nSorted Array is:")
print(data)
