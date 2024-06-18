def insertionSort(arr):
    n = len(arr) #calculates length of the array

    if n <= 1:
        return #if the array has 0 or 1 element, its already sorted

    for i in range(1,n):
        key = arr[i]
        j= i-1
        
        while j >=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr [j+1] = key

arr= [44,22,11,55,99,66,88]

insertionSort(arr)
print(arr)
