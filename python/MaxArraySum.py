def maxSubsetSum(arr, table = {}):
    table[0] = arr[0]
    table[1] = max(arr[0], arr[1])
    
    i = 2
    for el in arr[2:]:
        table[i] = max(table[i-1], table[i-2], el ,table[i-2] + el)
        i = i + 1    
                    
    return table[len(arr)-1]    
