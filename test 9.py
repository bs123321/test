string = input().split(" ")

"""
сортировка пузырь
"""
numbers = []

for i in string:
    numbers.append(int(i))
numbers.sort()

print(numbers)





# if int(string[0]) == int(string[1]):
#     print("числа равные", string[0])
# else:
#     if int(string[0]) > int(string[1]):
#         print("второе число: ", int(string[1]))
#         print("первое число: ", int(string[0]))
#     else:
#         print("первое число: ", int(string[0]))
#         print("второе число: ", int(string[1]))
