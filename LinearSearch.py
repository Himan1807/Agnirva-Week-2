def linear_search(arr, target):
    for i in range(0, len(arr), 1):
        if(arr[i] == target):
            return i
    return "Target not found"

dataset = [5, 3, 7, 1, 8, 9]
target = 1
print(linear_search(dataset, target))