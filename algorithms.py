def single_linear_s(array, start, size, key):
    for i in range(start, size):
        if array[i] == key:
            return i
    return -1

def single_binary_s(array, start, end, key):
    if start > end:
        return -1
    middle = start + (end - start) // 2
    if array[middle] == key:
        return middle
    elif array[middle] > key:
        return single_binary_s(array, start, middle-1, key)
    return single_binary_s(array, middle+1, end, key)

def merge(array, low, mid, high): # сортировка слиянием
    b = [None]*(high+1-low)
    h = low
    i = 0
    j = mid+1
    while h <= mid and j <= high:
        if array[h] <= array[j]:
            b[i] = array[h]
            h += 1
        else:
            b[i] = array[j]
            j += 1
        i += 1
    if h > mid:
        for k in range(j, high+1):
            b[i] = array[k]
            i += 1
    else:
        for k in range(h, mid+1):
            b[i] = array[k]
            i += 1
    for k in range(high-low+1):
        array[k+low] = b[k]
    return array

def merge_sort(array, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)
    return array
