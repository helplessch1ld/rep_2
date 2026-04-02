def linear_sort_no_arr(arr, ascending=True):
    n = len(arr)
    result = arr.copy()
    
    for i in range(n):
        extremum_idx = i
        for j in range(i + 1, n):
            if ascending:
                if result[j] < result[extremum_idx]:
                    extremum_idx = j
            else:
                if result[j] > result[extremum_idx]:
                    extremum_idx = j
        
        if extremum_idx != i:
            result[i], result[extremum_idx] = result[extremum_idx], result[i]
    
    return result

