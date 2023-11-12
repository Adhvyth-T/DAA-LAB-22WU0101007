def custom_sort(matrix):
    flattened_matrix = [element for row in matrix for element in row]
    flattened_matrix.sort()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = flattened_matrix.pop(0)

def replace_diagonals_with_zeros(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0

    for i in range(len(matrix)):
        matrix[i][len(matrix) - i - 1] = 0

matrix = [
    [5, 3, 8],
    [2, 7, 1],
    [9, 4, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

custom_sort(matrix)

print("\nSorted Matrix:")
for row in matrix:
    print(row)

replace_diagonals_with_zeros(matrix)

print("\nMatrix with Diagonals Replaced:")
for row in matrix:
    print(row)
