def max_min(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return largest, smallest

arr = [2,4,1,55,32,6,7,8,9]

largest, smallest = max_min(arr)
print("Smallest:", smallest)
print("Largest:", largest)

