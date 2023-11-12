def find_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# Example usage:
arr = [1, 3, 5, 2, 7, 3, 8, 3]
target_number = 3
result = find_indices(arr, target_number)

if result:
    print(f"The number {target_number} occurs at indices:", result)
else:
    print(f"The number {target_number} does not exist in the array.")
