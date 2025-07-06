def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j   # arranging elements 

        arr[i], arr[min_index] = arr[min_index], arr[i] # swapping elements accordint to value in ascending order
    return arr  #returning the arranged array

# example
print(selection_sort([64, 25, 12, 22, 11]))