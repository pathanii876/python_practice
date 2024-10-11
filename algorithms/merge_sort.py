def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merged_left = merge_sort(left)
    merged_right = merge_sort(right)

    return merge(merged_left, merged_right)


def merge(left, right):
    print(len(left), len(right))
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

    # merged = []
    # i = 0  # Pointer for left array
    # j = 0  # Pointer for right array
    
    # # Merge the two arrays by comparing elements
    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         merged.append(left[i])
    #         i += 1
    #     else:
    #         merged.append(right[j])
    #         j += 1
    
    # # If there are remaining elements in the left array, append them
    # while i < len(left):
    #     merged.append(left[i])
    #     i += 1
    
    # # If there are remaining elements in the right array, append them
    # while j < len(right):
    #     merged.append(right[j])
    #     j += 1
    
    # return merged
    

arr = []
while True:
    ans= input("do you want to add element to list? Enter 'Y' or 'N' : ")
    if ans.upper() == 'N':
        break
    element = eval(input('Enter Element : '))
    arr.append(element)

sorted = merge_sort(arr)
print(sorted)