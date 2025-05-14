def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range (n - 1 - i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(target == arr[mid]):
            return mid
        elif(target < arr[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return -1

# taking list input as a string, then splitting it by spaces, converting them into int
list = list(map(int, input("Enter the numbers: ").split()))

# taking the target input
target = int(input("Enter the target: "))

# sort the list first
bubble_sort(list)
print("Sorted List: ", list)

# binary search on target
result = binary_search(target, list)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")