def merge_sort(arr1, arr2):
    merged = arr1 + arr2
    n = len(merged)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if merged[j] < merged[min]:
                min = j
        merged[i], merged[min] = merged[min], merged[i]  
    
    return merged


arr1 = [3, 2, 4]
arr2 = [1, 5, 6]
result = merge_sort(arr1, arr2)
print(f"Merged and sorted: {result}")
