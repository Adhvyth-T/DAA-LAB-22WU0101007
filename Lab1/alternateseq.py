def alternate_sort(arr):
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    output = []
    
    while left <= right:
        output.append(arr[left])
        
        left += 1
        
        if left <= right:
            output.append(arr[right])
            
 
            right -= 1
    
    return output


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = alternate_sort(arr)
print("Output sequence:", result)
