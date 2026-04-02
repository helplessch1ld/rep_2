def insertion_sort(arr, ascending=True):
    n = len(arr)
    result = arr.copy()
    
    for i in range(1, n):
        key = result[i]
        j = i - 1
        
        if ascending:
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
        else:
            while j >= 0 and result[j] < key:
                result[j + 1] = result[j]
                j -= 1
        
        result[j + 1] = key
    
    return result

