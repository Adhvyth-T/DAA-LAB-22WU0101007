def noDupl(arr):
    
    arr1=[]
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    arr=arr1
    print(arr)
    
noDupl([0,0,0,0])
