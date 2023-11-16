import math
import random


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

# stable
def bubble_sort_v1(arr):

    arr = arr.copy()
    size = len(arr)

    for i in range(0, size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# stable
def bubble_sort_v2(arr):
    
    arr = arr.copy()
    size = len(arr)
    
    for i in range(0, size):
        for j in range(size - 1, i, -1):
            if arr[j] <= arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


# stable
# taking into account if the array is already sorted
# or the remaining portion of the array is sorted
def bubble_sort_v3(arr):
    
    arr = arr.copy()
    size = len(arr)
    
    for i in range(0, size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# adding a key argument
# stable 
def bubble_sort(arr, /, *, key=None):
    
    arr = arr.copy()
    size = len(arr)
    
    if key is None:
        key = lambda value: value
    for i in range(0, size):
        for j in range(0, size - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# or this version to avoid unnecessary repeated function calls
# but results in more swap operation
def bubble_sort(arr, /, *, key=None):
    
    size = len(arr)
    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]
    
    for i in range(0, size):
        for j in range(0, size - i - 1):
            if key[j][1] > key[j + 1][1]:
                swap(key, j, j + 1)
    
    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr


# unstable
def selection_sort(arr, /, *, key=None):
    
    size = len(arr)
    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]
    
    for i in range(0, size):
        min = i
        for j in range(i + 1, size):
            if key[min][1] > key[j][1]:
                min = j
        swap(key, min, i)

    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr


# stable
def stable_selection_sort(arr, /, *, key=None):
 
    size = len(arr)
    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]
    
    for i in range(0, size):
        min = i
        for j in range(i + 1, size):
            if key[min][1] > key[j][1]:
                min = j
        min_key = key[min]
        for k in range(min, i, -1):
            key[k] = key[k - 1]
        key[i] = min_key
    
    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr


# stable
def insertion_sort(arr, /, *, key=None):
    
    size = len(arr)
    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]

    for i in range(1, size):
        if key[i][1] >= key[i - 1][1]:
            continue
        swap(key, i, i - 1)
        for j in range(i - 1, 0, -1):
            if key[j][1] >= key[j - 1][1]:
                break
            swap(key, j, j - 1)
    
    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr


# stable
def merge_sort(arr, /, *, key=None):
    
    def merge(start, middle, end):
        nonlocal temp, key

        i, j, k = start, middle + 1, start
        while (i <= middle) and (j <= end):
            if key[i][1] > key[j][1]:
                temp[k] = key[j]
                j += 1
            else:
                temp[k] = key[i]
                i += 1
            k += 1

        while i <= middle:
            temp[k] = key[i]
            i += 1
            k += 1
        
        while j <= end:
            temp[k] = key[j]
            j += 1
            k += 1
        
        for i in range(start, end + 1):
            key[i] = temp[i]

    def _merge_sort(start, end):
        
        if start >= end:
            return
        
        middle = start + (end - start) // 2
        _merge_sort(start, middle)
        _merge_sort(middle + 1, end)
        merge(start, middle, end)

    temp = [None] * len(arr)
    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]
    _merge_sort(0, len(arr) - 1)

    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr


# stable
def quick_sort(arr, /, *, key=None):
    
    def _quick_sort(start, end):
        nonlocal key
        
        if start >= end:
            return
        
        pivot = key[end]
        pivot_value = pivot[1]
        less_than_pivot = []
        greater_than_pivot = []
        for i in range(start, end):
            item = key[i]
            if item[1] <= pivot_value:
                less_than_pivot.append(item)
            else:
                greater_than_pivot.append(item)
        
        pivot_index = start + len(less_than_pivot)
        key[start:pivot_index] = less_than_pivot
        key[pivot_index] = pivot
        key[pivot_index + 1:end + 1] = greater_than_pivot
        
        _quick_sort(start, pivot_index - 1)
        _quick_sort(pivot_index + 1, end)

    if key is None:
        key = [(index, element) for index, element in enumerate(arr)]
    else:
        key = [(index, key(element)) for index, element in enumerate(arr)]

    _quick_sort(0, len(arr) - 1)
    sorted_arr = [arr[index] for index, _ in key]
    return sorted_arr



# stable 
# key must be a callable that returns an integer 
# or an object that can behave like an integer
# not suitable for arrays where 
# `(max(array) - min(array) - 1) / len(array)` is big
def counting_sort(arr, key=None):
    
    if len(arr) == 0:
        return arr

    if key is None:
        key = arr.copy()
    else:
        key = [key(element) for element in arr]

    max_, min_ = max(key), min(key)
    size = max_ - min_ + 1
    counts = [0] * size
    for element in key:
        counts[element - min_] += 1
    
    for i in range(1, size):
        counts[i] += counts[i - 1]
    
    sorted_arr = [None] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]
        key_value = key[i]
        rank = counts[key_value - min_] - 1
        sorted_arr[rank] = element
        counts[key_value - min_] -= 1
    
    return sorted_arr

