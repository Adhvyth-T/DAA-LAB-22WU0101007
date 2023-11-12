def middle_row_and_column_sum(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    middle_row = rows // 2

    middle_row_sum = sum(matrix[middle_row])

    middle_column = columns // 2

    middle_column_sum = sum(matrix[i][middle_column] for i in range(rows))

    return middle_row_sum, middle_column_sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

middle_row_sum, middle_column_sum = middle_row_and_column_sum(matrix)

print("Sum of the middle row:", middle_row_sum)
print("Sum of the middle column:", middle_column_sum)
print("sum of middle row and column is: ",middle_row_sum+middle_column_sum)
