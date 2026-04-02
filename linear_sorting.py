def linear_sort(arr, ascending=False):
    n = len(arr)
    arr_2 = [0] * n
    arr_copy = arr.copy()
    
    if ascending:
        compare = lambda x, y: x < y
        replace_with = max(arr_copy) + 1
    else:
        compare = lambda x, y: x > y
        replace_with = min(arr_copy) - 1
    
    for i in range(n):
        extremum_idx = 0
        extremum_val = arr_copy[0]
        
        for j in range(1, n):
            if compare(arr_copy[j], extremum_val):
                extremum_val = arr_copy[j]
                extremum_idx = j         
        
        if ascending:
            arr_2[i] = extremum_val
        else:
            arr_2[i] = extremum_val            
        
        arr_copy[extremum_idx] = replace_with
    
    return arr_2

