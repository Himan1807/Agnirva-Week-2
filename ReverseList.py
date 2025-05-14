numbers = [1, 2, 3, 4, 5]

# method - 2
length = len(numbers)
reversed_numbers = []
for i in range(length - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed List w/o using Reverse(): ", reversed_numbers)

# method - 1
# length = len(numbers)
# for i in range(0, int(length / 2), 1):
#     temp = numbers[length - i - 1]
#     numbers[length - 1 - i] = numbers[i]
#     numbers[i] = temp
# print("Reversed List w/o using Reverse(): ", numbers)