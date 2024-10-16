                                    # №1

# string = input().split(" ")
#
# begin = int(string[0])
# end = int(string[1])
#
# result = ""
#
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print(result)

                                    # №2

# string = input().split(" ")
# begin = int(string[0])
# end = int(string[1])

# result = ""
# for i in range(begin, end + 1):
#     result += str(i) + " "
# print(result)
#
# result = ""
# j = end
# for i in range(begin, end + 1):
#     result += str(j) + " "
#     j -= 1
# print(result)
#
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print(result)
#
# count = 0
# for i in range(begin, end+1):
#     if i % 5 == 0 and i != 0:
#         count+=1
# print(count)

                                    # №3

# string = input().split(" ")
# begin = int(string[0])
# end = int(string[1])
# result = ""
#
# for number in range(begin, end+1):
#     if number % 3 == 0 and number % 5 != 0:
#         result += "Fizz: " + str(number) + ", "
#     elif number % 5 == 0 and number % 3 != 0:
#         result += "Buzz: " + str(number) + ", "
#     elif number % 15 == 0:
#         result += "Fizz Buzz: " + str(number) + ", "
#     else:
#         result += "Num: " + str(number) + ", "
# print(result)
