def find_leaders(arr):
    n = len(arr)
 
    for i in range(n - 1, -1, -1):
      
        leader = arr[i]
        
        
        for j in range(i + 1, n):
            if leader < arr[j]:
                
                break
        else:
           
            print(leader, end=" ")


arr = [16, 17, 4, 3, 5, 2]
print("Leaders in the array:", end=" ")
find_leaders(arr)

def find_leaders(arr):
    n = len(arr)
 
    for i in range(n - 1, -1, -1):
      
        leader = arr[i]
        
        
        for j in range(i + 1, n):
            if leader < arr[j]:
                
                break
        else:
           
            print(leader, end=" ")


arr = [16, 17, 4, 3, 5, 2]
print("Leaders in the array:", end=" ")
find_leaders(arr)

