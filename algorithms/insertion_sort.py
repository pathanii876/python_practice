def insertion_sort(arr):
    j = 1

    while j < len(arr):
        i = j - 1
        temp = arr[j]
        while temp < arr[i] and i >= 0:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = temp
        j += 1
          
    return arr

list = [5,4,10,1,6,2]
sorted = insertion_sort(list)
print("original = ", list)
print("sorted = ",sorted)