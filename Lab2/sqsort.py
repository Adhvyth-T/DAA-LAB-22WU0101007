def counting_sort(arr):

    max_val = max(arr)
    #for frequency of each element
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

arr = [0, 0, 1, 2, 0, 1, 2, 2, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
