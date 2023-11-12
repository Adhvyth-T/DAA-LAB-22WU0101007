def find_triplets(arr, target_sum):
    n = len(arr)
    
    arr.sort()
    
   
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                triplet_sum = arr[i] + arr[j] + arr[k]
                
               
                if triplet_sum == target_sum:
                    print("Triplet found:", arr[i], arr[j], arr[k])
                    return  
    print("No triplet found with the specified sum.")

arr = [1, 4, 45, 6, 10, 8]
target_sum = 22
find_triplets(arr, target_sum)
