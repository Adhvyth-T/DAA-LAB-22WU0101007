def diagonalswap(matrix):
    f=0
    l=len(matrix)-1
    for i in range(len(matrix)):
        matrix[i][f],matrix[i][l]=matrix[i][l],matrix[i][f]
        f+=1
        l-=1
    print(matrix)
    
diagonalswap([[0,1,2],[3,4,5],[6,7,8]])