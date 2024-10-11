def divide(a, start, end):
    p = start+1
    q = end
    pivote = a[start]
    while q >= p:
        while p < len(a) and a[p] < pivote:
            print(p)
            p += 1

        while q >= 0 and a[q] > pivote:
            print(q)
            q -= 1

        if q < p:
            a[start], a[q] = a[q], a[start]
        else:
            a[p], a[q] = a[q], a[p]
    
    return q

def quick_sort(a, start, end):
    if start >= end:
        return None
    i = divide(a, start, end)

    quick_sort(a, start, i-1)
    quick_sort(a, i+1, end)



a = [1, -100, 0]
start = 0
end = len(a)-1
quick_sort(a, start, end)
print(a)