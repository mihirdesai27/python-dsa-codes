def move_zeros_to_end(arr):
    count = 0  # Count of non-zero elements
    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[count], arr[i] = arr[i], arr[count ] # Swap non-zero element to the front
            count += 1
    return arr

arr = [1,0,3,2,0,4,0,5]
result = move_zeros_to_end(arr)
print("Array after moving zeros to the end:", result)
    