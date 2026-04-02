import random 
def shuttle_sort(arr, ascending=True):    
    n = len(arr)
    result = arr.copy()
    
    for i in range(1, n):
        j = i
        while j > 0:
            if ascending:
                if result[j] < result[j - 1]:
                    result[j], result[j - 1] = result[j - 1], result[j]
                    j -= 1
                else:
                    break
            else:
                if result[j] > result[j - 1]:
                    result[j], result[j - 1] = result[j - 1], result[j]
                    j -= 1
                else:
                    break
    
    return result


