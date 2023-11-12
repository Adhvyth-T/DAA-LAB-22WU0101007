
N,D=list(map(int,input().split()))
listt=[]
for i in range(N):
    d,lect,curse=list(map(int,input().split()))
    listt.append([d,lect,curse])

def sort(arr):
    for i in range(len(arr)-1):

        for j in range(len(arr)-1):

            if arr[j][2]<arr[j+1][2]:

                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def eval(arr):
    curse=0
    
    array=[[-1,-1,-1],[-1,-1,-1]]
    
    for i in range(1,D+1):
        
        for j in arr:
            if j[0]==i:
                array.append(j)
        
        
        
        sort(array)
        array[0][1]-=1
        array=array+[[1,0,0] for k in range(len(array))]
        for m in array:
            if m[1]==0:
                array.remove(m)
            
            

    for j in array:
        if j[1] > 0:
            curse += j[2] * j[1]

    print(curse)

eval(listt)