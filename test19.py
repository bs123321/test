import re
s = input()

operation = re.findall(r'[(\-/\+*)]', s)
print(operation)
numbers= re.split(r'[(\-/\+*)]', s)
print(numbers)
j = 1
result = 0
while j < len(operation):
    for y in operation:
        if y == "+":
            result = numbers[j-1] + numbers[j]
    j += 1

print(result)



#
# if operation[0] == "+":
#     print(int(numbers[0]) + int(numbers[1]))
# elif operation[0] == "-":
#     print(int(numbers[0]) - int(numbers[1]))
# elif operation[0] == "*":
#     print(int(numbers[0]) * int(numbers[1]))
# elif operation[0] == "/":
#     print(int(numbers[0]) / int(numbers[1]))
#

