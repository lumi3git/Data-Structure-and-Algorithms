def bubblesort(elements):
    
    for n in range (len(elements)-1,0,-1):
        
        swapped = False
        
        for i in range(n):
            
            if elements[i] < elements[i+1]:
                swapped = True

                elements[i], elements[i+1] = elements[i+1], elements[i]

                if not swapped:
                    return

elements = [120,888,755,558,936,133]

print("Unsorted List is: ")
print(elements)

bubblesort(elements)

print("\nSorted Array is: ")
print(elements)
