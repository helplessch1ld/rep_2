def bubble_sort(arr, ascending=True):   
    n = len(arr)
    result = arr.copy()
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if ascending:
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            else:
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
        
        if not swapped:
            break
   
    return result
