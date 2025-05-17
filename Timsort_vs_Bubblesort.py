import time, random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

numbers = [random.randint(1, 1000) for _ in range(1000)]
start_time = time.time()
bubble_sort(numbers.copy())
end_time = time.time()

print("Bubble Sort time: ", end_time - start_time)

start_time = time.time()
numbers.sort()
end_time = time.time()
print("Python's Built-in Timsort time: ", end_time - start_time)