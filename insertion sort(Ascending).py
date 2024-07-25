def insertionSort(arr):
    n = len(arr)  # calculates the length of the array

    if n <= 1:
        return  # if the array has 0 or 1 element, it's already sorted

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"Inserting {key} into the sorted portion of the array")

        
        print("Before insertion:", arr[:i], "|", arr[i:]) # Print the array state before insertion

        while j >= 0 and key < arr[j]:  # Inner Loop for Shifting Elements
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        
        print("After insertion: ", arr[:i+1], "|", arr[i+1:]) # Print the array state after insertion
        print()  # Blank line for readability


#In here, 4 is the already sorted array, we're going to insert 9, 26, 78, 63, 75 respectively
arr = [4, 9, 26, 78, 63, 75]

print("Sorted Array:", arr)
print()

insertionSort(arr)

print("Sorted Array after the insertion of new elements from 9:", arr)
