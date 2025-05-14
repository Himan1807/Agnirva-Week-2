def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(n - 1 - i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break


numbers = [50, 20, 40, 10, 30]
bubble_sort(numbers)
print("Sorted list:", numbers)  # Output: [10, 20, 30, 40, 50]