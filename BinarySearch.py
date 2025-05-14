def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == target):
            return mid
        elif(target < arr[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return "Target not found"

sorted_dataset = [1, 3, 5, 7, 8, 9]
target = 0
print(binary_search(target, sorted_dataset))  